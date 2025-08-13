from datetime import datetime
import pandas as pd
import os
import re


class Tache:
    compteur = 0
    def __init__(self, nom: str, date_fin: str):
        self.nom = nom
        self.date_creation = datetime.now()
        self.date_fin = datetime.strptime(date_fin, "%d-%m-%Y, %H:%M:%S")
        Tache.compteur += 1
        self.id = Tache.compteur
        self.statut = self.verifier_statut()

    def verifier_statut(self):
        return "En cours" if datetime.now() < self.date_fin else "Non faite"

    def to_dict(self):
        return {
            "id": self.id,
            "Nom": self.nom,
            "Statut": self.statut,
            "Date debut": self.date_creation.strftime('%d-%m-%Y, %H:%M:%S'),
            "Date fin": self.date_fin.strftime('%d-%m-%Y, %H:%M:%S')
        }


class GestionnaireTaches:
    FICHIER = "taches.xlsx"

    def __init__(self):
        self.fichier = self.FICHIER

        if not os.path.exists(self.fichier):
                    colonnes = ["id", "Nom", "Statut", "Date debut", "Date fin"]
                    df_vide = pd.DataFrame(columns=colonnes)
                    df_vide.to_excel(self.fichier, index=False)
            
    def ajouter_tache(self, nom: str, date_fin: str):
        df = pd.read_excel(self.fichier)
        Tache.compteur = len(df)
        tache = Tache(nom, date_fin)
        df = pd.concat([df, pd.DataFrame([tache.to_dict()])], ignore_index=True)
        df.to_excel(self.fichier, index=False)
        print(f"Tâche ajoutée : {tache.nom}")

    def afficher_taches(self):
        df = pd.read_excel(self.fichier)
        if df.empty:
            print("Aucune tâche enregistrée.")
            return
        print("\nListe des tâches :")
        for _, ligne in df.iterrows():
            description = ", ".join([f"{k}: {v}" for k, v in ligne.items()])
            print(f"→ {description}")

    def trouver_tache(self, identifiant):
        df = pd.read_excel(self.fichier)
        try:
            identifiant = int(identifiant)
            ligne = df[df["id"] == identifiant]
        except ValueError:
            identifiant = ''.join(re.findall(r'[a-zA-Z]+', identifiant)).lower()
            ligne = df[df["Nom"].str.lower() == identifiant]

        if not ligne.empty:
            return ligne.index[0]
        return None

    def marquer_faite(self, identifiant):
        index = self.trouver_tache(identifiant)
        if index is not None:
            df = pd.read_excel(self.fichier)
            df.at[index, "Statut"] = "Faite"
            df.to_excel(self.fichier, index=False)
            print(f"Tâche marquée comme faite : {df.at[index, 'Nom']}")
        else:
            print("Tâche non trouvée.")

    def modifier_tache(self, identifiant, nouvelle_date_fin):
        index = self.trouver_tache(identifiant)
        if index is not None:
            try:
                nouvelle_date = datetime.strptime(nouvelle_date_fin, "%d-%m-%Y, %H:%M:%S")
                df = pd.read_excel(self.fichier)
                df.at[index, "Date fin"] = nouvelle_date.strftime('%d-%m-%Y, %H:%M:%S')
                df.at[index, "Statut"] = "En cours" if datetime.now() < nouvelle_date else "Non faite"
                df.to_excel(self.fichier, index=False)
                print(f"Date de fin modifiée pour la tâche : {df.at[index, 'Nom']}")
            except ValueError:
                print("Format de date invalide.")
        else:
            print("Tâche non trouvée.")

    def supprimer_tache(self, identifiant):
        index = self.trouver_tache(identifiant)
        if index is not None:
            df = pd.read_excel(self.fichier)
            nom = df.at[index, "Nom"]
            df.drop(index, inplace=True)
            df.reset_index(drop=True, inplace=True)
            df.to_excel(self.fichier, index=False)
            print(f"Tâche supprimée : {nom}")
        else:
            print("Tâche non trouvée.")


class InterfaceUtilisateur:
    def __init__(self):
        self.gestionnaire = GestionnaireTaches()

    def executer(self):
        while True:
            print("\n=== MENU DU GESTIONNAIRE DE TÂCHES ===")
            print("1. Ajouter une tâche")
            print("2. Marquer une tâche comme faite")
            print("3. Modifier une tâche")
            print("4. Supprimer une tâche")
            print("5. Afficher toutes les tâches")
            print("6. Quitter")

            choix = input("Entrez votre choix : ").strip()

            if choix == '1':
                nom = input("Nom de la tâche : ")
                date_fin = input("Date de fin (ex : 24-07-2025, 23:30:00) : ")
                self.gestionnaire.ajouter_tache(nom, date_fin)

            elif choix == '2':
                self.gestionnaire.afficher_taches()
                identifiant = input("Entrez l'identifiant ou le nom de la tâche : ")
                self.gestionnaire.marquer_faite(identifiant)

            elif choix == '3':
                self.gestionnaire.afficher_taches()
                identifiant = input("Entrez l'identifiant ou le nom de la tâche : ")
                nouvelle_date = input("Nouvelle date de fin (ex : 25-07-2025, 20:00:00) : ")
                self.gestionnaire.modifier_tache(identifiant, nouvelle_date)

            elif choix == '4':
                self.gestionnaire.afficher_taches()
                identifiant = input("Entrez l'identifiant ou le nom de la tâche à supprimer : ")
                self.gestionnaire.supprimer_tache(identifiant)

            elif choix == '5':
                self.gestionnaire.afficher_taches()

            elif choix == '6':
                print("Au revoir.")
                break

            else:
                print("Choix invalide. Veuillez entrer un numéro de 1 à 6.")


def main():
    interface = InterfaceUtilisateur()
    interface.executer()


if __name__ == "__main__":
    main()

