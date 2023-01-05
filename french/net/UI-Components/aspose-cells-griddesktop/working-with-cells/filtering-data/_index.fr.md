---
title: Filtrage des données
type: docs
weight: 100
url: /fr/net/filtering-data/
---
{{% alert color="primary" %}} 

**Aspose.Cells.GridDesktop** fournit des fonctionnalités de filtre automatique et de filtre de données personnalisé pour les utilisateurs. À l'aide de ces fonctionnalités, vous pouvez trouver un moyen de sélectionner uniquement les éléments de la feuille de calcul que vous souhaitez afficher dans une liste. De plus, vous êtes autorisé à filtrer les éléments d'une liste selon un ensemble de critères. Vous pouvez filtrer du texte, des nombres ou des dates avec la fonction Filtre automatique / Filtre de données personnalisé.

 Vous pouvez utiliser**Activer le filtre automatique** Attribut booléen de**RowFilterSettings** classe pour activer la fonctionnalité de filtre automatique pour le contrôle GridDesktop. Il existe d'autres propriétés de la classe que vous pouvez utiliser, par exemple**Ligne d'en-tête** , **StartRow** et**EndRow**pour spécifier les index d'en-tête, de début et de fin de ligne. Le**Critère** La propriété est utilisée pour définir les critères de filtrage personnalisés. La classe a aussi une méthode nommée**Filtrer les lignes** pour obtenir les lignes filtrées en fonction des critères donnés.

 L'attribut de recherche de type "contient" (insensible à la casse) dans RowFilter est également pris en charge par GridDesktop. Vous pouvez utiliser**IgnorerCas** propriété de**GrilleColonne** class pour spécifier l'attribut de sensibilité à la casse pour votre besoin. Vous pouvez également utiliser une propriété nommée**IsStartWithCriteria** de**GrilleColonne** class pour indiquer si le RowFilter utilise le critère StartWith sur une colonne ; la valeur par défaut de la propriété est définie sur false.

{{% /alert %}} 
## **Filtrage des données**
Nous implémentons à la fois les fonctionnalités de filtre automatique et de filtre de données personnalisé dans cet exemple. Nous remplissons une liste de données dans GridDesktop, activons la fonction de filtre automatique, puis recherchons des lignes filtrées en fonction de certains critères.
### **Filtre automatique**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-AutoFilter.cs" >}}
### **Filtre de données personnalisé**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-CustomFilter.cs" >}}
