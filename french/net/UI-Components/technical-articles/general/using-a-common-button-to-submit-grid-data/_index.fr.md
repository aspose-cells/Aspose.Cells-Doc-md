---
title: Utilisation d un bouton commun pour soumettre les données de la grille
type: docs
weight: 20
url: /fr/net/aspose-cells-gridweb/using-a-common-button-to-submit-grid-data/
keywords: GridWeb, soumettre, bouton, personnalisé
description: Cet article décrit l utilisation d un bouton de soumission dans GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb fournit quelques boutons de commande intégrés tels que **Soumettre** et **Enregistrer**. Utilisez ces boutons pour effectuer des tâches connexes.

Cet article montre comment soumettre les données à un serveur non pas en cliquant sur le bouton de commande intégré **Enregistrer** de GridWeb, mais en cliquant sur un bouton ASP.NET commun (contrôle Web). Le but de cet article est de montrer la flexibilité d'Aspose.Cells.GridWeb. De plus, cet article utilise également des fonctions spéciales exposées par Aspose.Cells.GridWeb à utiliser dans le script côté client.

{{% /alert %}} 
## **Soumettre des données de la grille en utilisant un bouton ASP.NET**
Aspose.Cells.GridWeb fournit trois boutons intégrés (**Soumettre**, **Enregistrer** et **Annuler**). Après avoir modifié dans GridWeb, un utilisateur peut cliquer sur le bouton **Soumettre** ou **Enregistrer** dans la barre d'onglets pour permettre à GridWeb de soumettre les données au serveur. Si l'utilisateur clique sur un onglet de feuille, le contrôle GridWeb effectue la même tâche que celle des boutons de commande intégrés. Aspose.Cells.GridWeb prend également en charge l'ajout de cette fonctionnalité à un contrôle Button ASP.NET commun, mais vous devez ajouter un peu de code supplémentaire à l'application.
### **1. Création d'une application de test**
Ouvrez votre IDE Visual Studio.NET et créez un nouveau projet d'application Web ASP.NET. Une page par défaut WebForm1.aspx sera ajoutée à votre projet une fois l'application créée. Faites glisser et déposez le contrôle GridWeb depuis votre boîte à outils sur le formulaire Web. Si vous ne trouvez pas le contrôle GridWeb dans votre boîte à outils, consultez cette page : [Intégrer les contrôles de grille Aspose.Cells avec Visual Studio.NET](/cells/fr/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/) pour en savoir plus à ce sujet. Une fois le contrôle GridWeb ajouté à votre formulaire Web, ajoutez également un contrôle web Button depuis la boîte à outils à votre formulaire Web.
### **2. Ajout de code à l'événement Page_Load**
Maintenant, il est temps d'ajouter du code à l'événement Page_Load du formulaire Web. Vous pouvez double-cliquer sur le formulaire Web en mode design et l'IDE VS.NET vous amènera automatiquement à l'gestionnaire d'événements Page_Load où vous devrez utiliser la collection Attributes du Button pour remplacer son événement OnClick.

{{% alert color="primary" %}} 

Le contrôle Button ASP.NET est un contrôle côté serveur. Chaque fois qu'il est cliqué, un événement côté serveur est déclenché, mais si vous voulez utiliser ce contrôle Button pour exécuter du code côté client (normalement en utilisant javascript), alors vous devez modifier son attribut onclick sous l'événement Page_Load. Aspose.Cells.GridWeb fournit quelques fonctions qui peuvent être invoquées en javascript pour traiter le contrôle GridWeb côté client. Dans l'exemple ci-dessous, nous avons utilisé les fonctions updateData et validateAll (qui sont des fonctions côté client) de GridWeb pour mettre à jour et valider les données de la grille.

{{% /alert %}} 
#### **Exemple de code**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-UsingCommonSubmitButton.aspx-UsingCommonSubmitButton.cs" >}}
### **3. Exécution de l'application**
Maintenant, vous pouvez compiler et exécuter votre application en appuyant sur Ctrl+F5 et la page s'ouvrira dans une nouvelle fenêtre de navigateur. Ajoutez des valeurs à GridWeb et appuyez sur le bouton Soumettre les données de la grille au serveur et vous verrez un postback se produire pour mettre à jour et valider les données de GridWeb.
## **Conclusion**
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb offre une grande flexibilité pour travailler avec les contrôles GridWeb à partir du côté serveur ou client. Les développeurs ont un large éventail d'options pour utiliser le contrôle GridWeb dans différents scénarios afin de fournir de meilleures solutions à leurs clients.

{{% /alert %}}
