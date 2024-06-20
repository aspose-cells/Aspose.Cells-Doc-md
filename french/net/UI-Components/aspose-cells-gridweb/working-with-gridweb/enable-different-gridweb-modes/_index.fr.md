---
title: Activer les différents modes de GridWeb
type: docs
weight: 60
url: /fr/net/aspose-cells-gridweb/enable-different-gridweb-modes/
keywords: GridWeb,EditMode,SessionMode
description: Cet article présente comment travailler avec EditMode et SessionMode dans GridWeb.
---

{{% alert color="primary" %}} 

Cet article décrit les différents modes de Aspose.Cells.GridWeb. Ces modes sont différenciés logiquement en raison de leurs différentes fonctionnalités et comportements. Nous avons identifié plusieurs types de mode :

- Mode Édition
- Mode Affichage
- Mode Session
- Mode sans session

Tous ces modes ont leurs propres caractéristiques. Les développeurs peuvent travailler avec Aspose.Cells.GridWeb dans n'importe quel mode en fonction de leurs besoins. Nous examinerons chaque mode ci-dessous.

{{% /alert %}} 
## **Mode Édition**
Par défaut, le contrôle Aspose.Cells.GridWeb est en mode Édition. En mode Édition, vous pouvez entièrement modifier ou modifier le contenu de la grille en utilisant toutes les fonctionnalités offertes par le contrôle Aspose.Cells.GridWeb. Ces fonctionnalités comprennent :

- Enregistrer le contenu de la grille dans des fichiers Microsoft Excel.
- Envoyer des données à un serveur.
- Calculer des formules.
- Annuler ou rejeter des actions précédentes.
- Gérer les lignes et les colonnes.
- Couper, copier ou coller des données.
- Mise en forme des cellules, etc.

**Contrôle GridWeb en mode édition** 

![todo:image_alt_text](enable-different-gridweb-modes_1.png)

Les développeurs peuvent également passer en mode Édition de manière programmée en définissant la propriété EditMode du contrôle GridWeb sur true.

L'exemple ci-dessous montre comment activer le mode d'édition de manière programmatique.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyEditMode.cs" >}}

{{% alert color="primary" %}} 

Chaque fois qu'un utilisateur clique sur le bouton **Annuler**, il ramène GridWeb à son état précédent (l'état avant le dernier renvoi au serveur). Il n'annule pas les actions précédentes une par une.

{{% /alert %}} 
## **Mode visualisation**
Lorsque le contrôle GridWeb est en mode Vue, les utilisateurs ne peuvent pas modifier le contenu de la grille, ce qui signifie qu'ils ne peuvent que le visualiser. C'est pourquoi ce mode est appelé mode Vue. En mode Vue, quelques boutons (**Soumettre**, **Enregistrer** et **Annuler**) sont cachés et le menu qui apparaît lors d'un clic droit ne contient que l'option **Copier**.

**Contrôle GridWeb en mode visualisation** 

![todo:image_alt_text](enable-different-gridweb-modes_1.png)

Si les développeurs souhaitent que leurs utilisateurs ne visualisent que les données, ils peuvent passer en mode Vue de manière programmée en définissant la propriété EditMode du contrôle GridWeb sur false.

L'exemple ci-dessous montre comment activer le mode vue de manière programmée



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyViewMode.cs" >}}

{{% alert color="primary" %}} 

Même en mode visualisation, les utilisateurs peuvent modifier la hauteur et la largeur des lignes et des colonnes.

{{% /alert %}} 
## **Mode Session**
Le contrôle Aspose.Cells.GridWeb conserve les données de la feuille dans la session utilisateur du serveur Web entre chaque requête d'un utilisateur Web. Cela signifie que le contrôle GridWeb fonctionne toujours en mode Session par défaut. Cependant, si vous ne travaillez pas en mode Session, activez-le en définissant la propriété SessionMode du contrôle GridWeb sur SessionMode.Session.

L'exemple ci-dessous montre comment activer le mode session de manière programmée



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionMode.cs" >}}
## **Mode sans session**
Nous avons déjà discuté que l'approche du mode Session offre les meilleures performances en utilisant une session utilisateur pour charger et stocker les données de la feuille. Cependant, cela consomme de la mémoire serveur. Donc, s'il y a un grand nombre d'utilisateurs simultanés, des problèmes de mémoire peuvent survenir. Pour économiser la mémoire serveur et prendre en charge un grand nombre d'utilisateurs simultanés, envisagez le mode sans session.

Le mode sans session peut être activé en définissant la propriété SessionMode du contrôle GridWeb sur SessionMode.ViewState.

L'exemple ci-dessous montre comment activer le mode sans session de manière programmée



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionlessMode.cs" >}}

{{% alert color="primary" %}} 

IMPORTANT : Lorsque la propriété SessionMode du GridWeb est définie sur SessionMode.ViewState, la grille stocke les données dans le ViewState de la page. Cela signifie que la page rendue est plus grande, et consomme plus de trafic réseau.

{{% /alert %}} {{% alert color="primary" %}} 

Si vous souhaitez utiliser SQL Server ou StateServer pour stocker des sessions, utilisez le mode Session. Le contrôle GridWeb prend en charge la sérialisation de ses données vers SQL Server ou StateServer.

Veuillez consulter l'article suivant pour plus d'aide.

- [Fonctionnement de GridWeb lorsque le mode d'état de session ASP.NET est SQL Server](/cells/fr/net/aspose-cells-gridweb/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/)

{{% /alert %}}
