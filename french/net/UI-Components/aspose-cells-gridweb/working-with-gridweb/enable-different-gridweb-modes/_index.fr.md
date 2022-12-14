---
title: Activer différents modes GridWeb
type: docs
weight: 60
url: /fr/net/enable-different-gridweb-modes/
---
{{% alert color="primary" %}} 

Cet article décrit les différents modes de Aspose.Cells.GridWeb. Ces modes se différencient logiquement en raison de leurs caractéristiques et comportements différents. Nous avons identifié plusieurs types de mode :

- Mode édition
- Mode d'affichage
- Mode session
- Mode sans session

Tous ces modes ont leurs propres caractéristiques. Les développeurs peuvent travailler avec Aspose.Cells.GridWeb dans n'importe quel mode en fonction de leurs besoins. Nous examinerons chaque mode ci-dessous.

{{% /alert %}} 
## **Mode édition**
Par défaut, le contrôle Aspose.Cells.GridWeb est en mode Edition. En mode Édition, vous pouvez entièrement éditer ou modifier le contenu de la grille en utilisant toutes les fonctionnalités offertes par le contrôle Aspose.Cells.GridWeb. Ces fonctionnalités incluent :

- Enregistrement du contenu de la grille dans des fichiers Excel Microsoft.
- Envoi de données à un serveur.
- Formules de calcul.
- Annuler ou supprimer les actions précédentes.
- Gestion des lignes et des colonnes.
- Couper, copier ou coller des données.
- Formatage des cellules, etc.

**Contrôle GridWeb en mode édition** 

![tâche : image_autre_texte](enable-different-gridweb-modes_1.png)

Les développeurs peuvent également passer en mode édition par programmation en définissant la propriété EditMode du contrôle GridWeb sur true.

L'exemple ci-dessous montre comment activer le mode d'édition par programmation.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyEditMode.cs" >}}

{{% alert color="primary" %}} 

 Chaque fois qu'un utilisateur clique sur le**annuler** , il ramène le GridWeb à son état précédent (l'état avant la dernière publication sur le serveur). Il n'annule pas les actions précédentes une par une.

{{% /alert %}} 
## **Mode d'affichage**
Lorsque le contrôle GridWeb est en mode Affichage, les utilisateurs ne peuvent pas éditer ou modifier le contenu de la grille, ce qui signifie qu'ils peuvent uniquement afficher le contenu de la grille. C'est pourquoi ce mode s'appelle le mode Affichage. En mode Afficher, quelques boutons (**Soumettre**, **sauvegarder** et**annuler** ) sont masqués et le menu qui apparaît lors d'un clic droit ne contient que les**Copie** option.

**Contrôle GridWeb en mode Affichage** 

![tâche : image_autre_texte](enable-different-gridweb-modes_1.png)

Si les développeurs souhaitent que leurs utilisateurs n'affichent que les données, ils peuvent passer en mode Affichage par programmation en définissant la propriété EditMode du contrôle GridWeb sur false.

L'exemple ci-dessous montre comment activer le mode d'affichage par programme



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyViewMode.cs" >}}

{{% alert color="primary" %}} 

Même en mode Affichage, les utilisateurs peuvent modifier la hauteur et la largeur des lignes et des colonnes.

{{% /alert %}} 
## **Mode session**
Le contrôle Aspose.Cells.GridWeb contient des données de feuille dans la session utilisateur du serveur Web entre chaque requête d'un utilisateur Web. Cela signifie que le contrôle GridWeb fonctionne toujours en mode Session par défaut. Toutefois, si vous ne travaillez pas en mode Session, activez-le en définissant la propriété SessionMode du contrôle GridWEb sur SessionMode.Session.

L'exemple ci-dessous montre comment activer le mode session par programmation



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionMode.cs" >}}
## **Mode sans session**
Nous avons déjà expliqué que l'approche du mode Session offre les meilleures performances en utilisant une session utilisateur pour charger et stocker les données de la feuille. Cependant, il consomme de la mémoire serveur. Ainsi, s'il y a un grand nombre d'utilisateurs simultanés, des problèmes de mémoire peuvent survenir. Pour économiser la mémoire du serveur et prendre en charge un grand nombre d'utilisateurs simultanés, envisagez le mode sans session.

Le mode sans session peut être activé en définissant la propriété SessionMode du contrôle GridWeb sur SessionMode.ViewState.

L'exemple ci-dessous montre comment activer le mode sans session par programmation



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionlessMode.cs" >}}

{{% alert color="primary" %}} 

IMPORTANT : Lorsque la propriété SessionMode de GridWeb est définie sur SessionMode.ViewState, la grille stocke les données dans le ViewState de la page. Cela signifie que la page rendue est plus grande et consomme plus de trafic réseau.

{{% /alert %}} {{% alert color="primary" %}} 

Si vous souhaitez utiliser SQL Server ou StateServer pour tenir des sessions, utilisez le mode Session. Le contrôle GridWeb prend en charge la sérialisation de ses données vers SQL Server ou StateServer.

Veuillez consulter l'article suivant pour plus d'aide.

- [Fonctionnement de GridWeb lorsque le mode d'état de session ASP.NET est SQL Server](/cells/fr/net/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/)

{{% /alert %}}
