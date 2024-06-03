# Diagramme de Cas d'Utilisation

Voici un diagramme de cas d'utilisation pour l'application de gestion de matériel :

```mermaid
graph TD;
    A[Utilisateur] --> B[Ajouter un Enseignant]
    A --> C[Ajouter un Matériel]
    A --> D[Changer le Possesseur d'un Matériel]
    A --> E[Afficher la Liste des Matériels par Salle]
    A --> F[Afficher la Liste des Matériels par Responsable]
    A --> G[Afficher l'Historique d'un Matériel]
    A --> H[Afficher la Liste des Matériels]
    A --> I[Gestion des Utilisateurs et Authentification]

    B --> J[Formulaire de Création]
    C --> K[Formulaire de Création]
    D --> L[Formulaire de Changement]
    E --> M[Vue de Liste]
    F --> N[Vue de Liste]
    G --> O[Vue d'Historique]
    H --> P[Vue de Liste]
    I --> Q[Création et Gestion de Comptes]
    I --> R[Authentification]
    I --> S[Gestion des Rôles et Permissions]
