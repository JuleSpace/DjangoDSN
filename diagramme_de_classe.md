classDiagram
    class Enseignant {
        - id: Integer
        - nom: String
        - prenom: String
        + ajouter(): void
        + supprimer(): void
    }

    class Salle {
        - id: Integer
        - numero: String
        + ajouter(): void
        + supprimer(): void
    }

    class Materiel {
        - id: Integer
        - nom: String
        - type: String
        - budget: String
        - responsable: Enseignant
        - localisation: Salle
        - possesseur: Enseignant
        - accessoires: String
        + ajouter(): void
        + supprimer(): void
        + changerPossesseur(nouveauPossesseur: Enseignant, nouvelleSalle: Salle): void
        + localiser(): Salle
    }

    class Historique {
        - id: Integer
        - materiel: Materiel
        - ancienPossesseur: Enseignant
        - nouveauPossesseur: Enseignant
        - date: Date
        - lieu: Salle
        - occasion: String
        - etatAccessoires: String
        + ajouter(): void
        + supprimer(): void
    }

    Enseignant "1" <-- "0..*" Materiel : responsable
    Enseignant "1" <-- "0..*" Materiel : possesseur
    Salle "1" <-- "0..*" Materiel : localisation
    Materiel "1" <-- "0..*" Historique : materiel
    Enseignant "1" <-- "0..*" Historique : ancienPossesseur
    Enseignant "1" <-- "0..*" Historique : nouveauPossesseur
    Salle "1" <-- "0..*" Historique : lieu
