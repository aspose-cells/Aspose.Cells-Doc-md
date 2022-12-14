---
title: Utilisation d'un bouton commun pour soumettre des données de grille
type: docs
weight: 20
url: /fr/net/using-a-common-button-to-submit-grid-data/
---
{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb fournit des boutons de commande intégrés tels que**Soumettre** et**sauvegarder**. Utilisez ces boutons pour effectuer des tâches connexes.

Cet article montre comment soumettre des données à un serveur non seulement en cliquant sur le bouton intégré de GridWeb**sauvegarder** bouton de commande, mais en cliquant sur un bouton ASP.NET commun (Contrôle Web). Le but de cet article est de montrer la flexibilité de Aspose.Cells.GridWeb. De plus, cet article utilise également des fonctions spéciales exposées par Aspose.Cells.GridWeb à utiliser dans le script côté client.

{{% /alert %}} 
## **Envoi de données de grille à l'aide d'un bouton ASP.NET**
Aspose.Cells.GridWeb fournit trois boutons intégrés (**Soumettre**, **sauvegarder** et**annuler** ). Après l'édition dans GridWeb, un utilisateur peut cliquer sur le**Soumettre** ou**sauvegarder** dans la barre d'onglets pour permettre à GridWeb de soumettre des données au serveur. Si l'utilisateur clique sur un onglet de feuille, le contrôle GridWeb effectue la même tâche que celle des boutons de commande intégrés. Aspose.Cells.GridWeb prend également en charge l'ajout de cette fonctionnalité à un contrôle Button ASP.NET commun, mais vous devez ajouter du code supplémentaire à l'application.
### **1. Création d'une application de test**
Ouvrez votre IDE Visual Studio.NET et créez un nouveau projet d'application Web ASP.NET. Une fois l'application créée, une page WebForm1.aspx par défaut sera ajoutée à votre projet. Faites glisser et déposez le contrôle GridWeb de votre boîte à outils vers le formulaire Web. Si vous ne trouvez pas le contrôle GridWeb dans votre boîte à outils, reportez-vous à cette page :[Intégrer les contrôles de grille Aspose.Cells à Visual Studio.NET](/cells/fr/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/) pour en savoir plus. Une fois le contrôle GridWeb ajouté à votre formulaire Web, ajoutez également un contrôle Web Button de Toolbox à votre formulaire Web.
### **2. Ajout de code à l'événement Page_Load**
Maintenant, il est temps d'ajouter du code à Page_Charger l'événement du formulaire Web. Vous pouvez double-cliquer sur le formulaire Web en mode conception et VS.NET IDE vous amènera automatiquement à la page_Charger le gestionnaire d'événements où vous auriez besoin d'utiliser la collection Attributes du bouton pour remplacer son événement OnClick.

{{% alert color="primary" %}} 

ASP.NET Le contrôle Button est un contrôle côté serveur. Chaque fois qu'il est cliqué, un événement côté serveur est déclenché, mais si vous souhaitez utiliser ce contrôle Button pour exécuter du code côté client (normalement en utilisant javascript), vous devez modifier son attribut onclick sous l'événement Page_Load. Aspose.Cells.GridWeb fournit certaines fonctions qui peuvent être invoquées en javascript pour gérer le contrôle GridWeb du côté client. Dans l'exemple ci-dessous, nous avons utilisé les fonctions updateData & validateAll (qui sont des fonctions côté client) de GridWeb pour mettre à jour et valider les données de Grid.

{{% /alert %}} 
#### **Exemple de code**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-UsingCommonSubmitButton.aspx-UsingCommonSubmitButton.cs" >}}
### **3. Exécution de l'application**
Maintenant, vous pouvez compiler et exécuter votre application en appuyant sur Ctrl+F5 et la page s'ouvrira dans une nouvelle fenêtre de navigateur. Ajoutons quelques valeurs à GridWeb et appuyez sur le bouton Submit Grid Data to Server et vous verrez se produire une publication pour mettre à jour et valider les données GridWeb.
## **Conclusion**
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb offre une grande flexibilité pour travailler avec les contrôles GridWeb du côté serveur ou client. Les développeurs disposent d'un grand nombre d'options pour utiliser le contrôle GridWeb dans différents types de scénarios afin de fournir de meilleures solutions à leurs clients.

{{% /alert %}}
