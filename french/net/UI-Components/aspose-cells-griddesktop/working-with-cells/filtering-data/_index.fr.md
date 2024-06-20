---
title: Filtrage des données
type: docs
weight: 100
url: /fr/net/aspose-cells-griddesktop/filtering-data/
keywords: GridDesktop, filtre, filtre de données, AutoFiltre, FiltreLigne
description: Cet article présente comment filtrer les données dans la feuille de calcul dans GridDesktop.
---

{{% alert color="primary" %}} 

**Aspose.Cells.GridDesktop** fournit des fonctionnalités de filtre automatique et de filtre de données personnalisé pour les utilisateurs. En utilisant ces fonctionnalités, vous pouvez sélectionner uniquement les éléments de la feuille de calcul que vous souhaitez afficher dans une liste. De plus, vous êtes autorisé à filtrer les éléments dans une liste selon des critères définis. Vous pouvez filtrer du texte, des nombres ou des dates avec la fonctionnalité de filtre automatique / filtre de données personnalisé.

Vous pouvez utiliser l'attribut booléen **EnableAutoFilter** de la classe **RowFilterSettings** pour activer la fonctionnalité de filtre automatique pour le contrôle GridDesktop. Il y a d'autres propriétés de la classe que vous pouvez utiliser, par exemple **HeaderRow**, **StartRow** et **EndRow** pour spécifier les indexes de l'en-tête, de début et de fin. La propriété **Criteria** est utilisée pour définir les critères de filtrage personnalisé. La classe a également une méthode appelée **FilterRows** pour obtenir les lignes filtrées en fonction des critères donnés.

L'attribut de recherche de type "contains" (insensible à la casse) dans RowFilter est également pris en charge par GridDesktop. Vous pouvez utiliser la propriété **IgnoreCase** de la classe **GridColumn** pour spécifier l'attribut de sensibilité à la casse selon vos besoins. Vous pouvez également utiliser une propriété nommée **IsStartWithCriteria** de la classe **GridColumn** pour indiquer si le RowFilter utilise les critères de début sur une colonne; la valeur par défaut de la propriété est définie sur false.

{{% /alert %}} 
## **Filtrage de données**
Nous mettons en œuvre à la fois les fonctionnalités de filtre automatique et de filtre de données personnalisé dans cet exemple. Nous remplissons une liste de données dans le GridDesktop, activons la fonctionnalité de filtre automatique, puis recherchons des lignes filtrées en fonction de certains critères.
### **Filtre automatique**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-AutoFilter.cs" >}}
### **Filtre de données personnalisé**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-CustomFilter.cs" >}}
