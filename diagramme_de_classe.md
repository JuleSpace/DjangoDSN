# Diagramme de Classe

Voici le diagramme de classe pour l'application de gestion de matériel :

```mermaid
classDiagram
    class Enseignant {
        int id
        String nom
        String prenom
        void ajouter()
        void supprimer()
    }

    class Salle {
        int id
        String numero
        void ajouter()
        void supprimer()
    }

    class Materiel {
        int id
        String nom
        String type
        String budget
        Enseignant responsable
        Salle localisation
        Enseignant possesseur
        String accessoires
        void ajouter()
        void supprimer()
        void changerPossesseur(Enseignant nouveauPossesseur, Salle nouvelleSalle)
        Salle localiser()
    }

    class Historique {
        int id
        Materiel materiel
        Enseignant ancienPossesseur
        Enseignant nouveauPossesseur
        Date date
        Salle lieu
        String occasion
        String etatAccessoires
        void ajouter()
        void supprimer()
    }

    Enseignant "1" --> "0..*" Materiel : responsable
    Enseignant "1" --> "0..*" Materiel : possesseur
    Salle "1" --> "0..*" Materiel : localisation
    Materiel "1" --> "0..*" Historique : materiel
    Enseignant "1" --> "0..*" Historique : ancienPossesseur
    Enseignant "1" --> "0..*" Historique : nouveauPossesseur
    Salle "1" --> "0..*" Historique : lieu
