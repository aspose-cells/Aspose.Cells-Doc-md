---
title: Aspose.Cells for .NET 20.11 Notes de mise à jour
type: docs
weight: 2
url: /fr/net/aspose-cells-for-net-20-11-release-notes/
---
{{% alert color="primary" %}}

 Cette page contient des notes de version pour[Aspose.Cells for .NET 20.11](https://www.nuget.org/packages/Aspose.Cells/20.11.0).

{{% /alert %}}

|**Clé**|**Sommaire**|**Catégorie**|
|:- |:- |:- |
|CELLSNET-47706|Prise en charge du modèle de formatage dépendant des paramètres régionaux "aaaa" pour l'année dans la région Espagne|Améliorations|
|CELLSNET-47641|Avertissement émis lors de l'ajout de 29 feuilles et de l'ouverture du fichier XLS de sortie dans MS Excel|Performance|
|CELLSNET-46716|Le texte a été coupé lors du rendu du PDF|Insectes|
|CELLSNET-47618|Une image devient toute blanche et une partie du texte est corrompue dans d'autres images/formes|Insectes|
|CELLSNET-47635| Un trancheur sur une table différente génère un fichier corrompu|Insectes|
|CELLSNET-47642|Le fichier XLSB est corrompu après le chargement et l'enregistrement|Insectes|
|CELLSNET-47660|Le champ de graphique contenant des dates a un format différent au format PDF|Insectes|
|CELLSNET-47661|Aspose.Cells génère un balisage HTML non valide pour une feuille de calcul particulière d'un document Cells particulier|Insectes|
|CELLSNET-47680|Les tableaux croisés dynamiques n'ont pas été actualisés|Insectes|
|CELLSNET-47659|Problème de recherche de cellules avec des styles spécifiques|Insectes|
|CELLSNET-47679|Différence de calcul entre Aspose.Cells et Excel|Insectes|
|CELLSNET-47666|Le classeur ne peut pas être affiché dans SharePoint|Insectes|
|CELLSNET-47698|Décalage de la position du logo lors de la conversion du fichier XLS en PDF|Insectes|
|CELLSNET-47651|L'exportation de la carte polaire au format pdf est faussée|Insectes|
|CELLSNET-47662|Des étiquettes de données incorrectes apparaissent lors de la conversion d'un graphique Excel en image|Insectes|
|CELLSNET-47667|Barres manquantes dans le graphique à barres de l'image de sortie|Insectes|
|CELLSNET-47697|Certaines valeurs de l'axe Y sortent du graphique dans le PDF de sortie|Insectes|
|CELLSNET-43579|La courbure du texte WortArt est modifiée lors de la conversion d'Excel en PDF|Insectes|
|CELLSNET-47675|Le contenu du fichier XLS est modifié après le chargement et l'enregistrement|Insectes|
|CELLSNET-47704|Les propriétés personnalisées ont disparu après avoir modifié/enregistré un fichier XLS protégé par mot de passe (crypté)|Insectes|
|CELLSNET-47708|L'ordre de tri ne fonctionnait pas correctement avec les formules dynamiques (Smart Markers)|Insectes|
|CELLSNET-47682|Exception lors du chargement d'un Htm particulier|Exceptions|
|CELLSNET-47683|Exception lors du chargement d'un Htm particulier|Exceptions|
|CELLSNET-47684|Exception lors du chargement d'un Htm particulier|Exceptions|
|CELLSNET-47689|Exception lors de la conversion de XLSB en PNG et HTML|Exceptions|
|CELLSNET-47701|Impossible de créer une copie du classeur XLTX|Exceptions|
|CELLSNET-47628|La suppression de lignes vides dans des cellules provoque une exception ArgumentOutOfRangeException|Exceptions|
|CELLSNET-47629|L'appel de valeurs de cellule après la suppression de lignes et de colonnes vides provoque ArgumentException|Exceptions|
|CELLSNET-47700|CalculateFormula lève InvalidCastException|Exceptions|
|CELLSNET-47703|Exception déclenchée lors de l'appel de Workbook.CalculateFormula()|Exceptions|
|CELLSNET-47669|L'index de colonne non valide ArgumentException est levé lors de la conversion de la 1ère feuille de calcul en HTML|Exceptions|
|CELLSNET-47677|DataBar.ToImage déclenche une exception si la ligne est masquée.|Exceptions|
|CELLSNET-47686|Impossible de convertir XLSB en XLSX|Exceptions|
|CELLSNET-47687|Impossible de charger les Ods|Exceptions|
|CELLSNET-47694|Exception lors de l'ouverture du fichier XLSX du document|Exceptions|
|CELLSNET-47695|Nom de cellule non valide après DeleteRange|Exceptions|
|CELLSNET-47699|Exception lors de l'ouverture du fichier ODS|Exceptions|
|CELLSNET-47702| Une exception s'est produite lors du chargement des fichiers chiffrés "Microsoft Excel 5.0/95 Workbook"|Exceptions|


## **Public API et modifications incompatibles avec les versions antérieures**

Voici une liste de toutes les modifications apportées au public API, telles que les membres ajoutés, renommés, supprimés ou obsolètes, ainsi que toute modification non rétrocompatible apportée à Aspose.Cells for .NET. Si vous avez des inquiétudes concernant l'un des changements répertoriés, veuillez le signaler sur le forum d'assistance Aspose.Cells.

### **Supprime la méthode obsolète CellsHelper.IsProtectedByRMS()**

Utilisez plutôt la propriété FileFormatUtil.DetectFileFormat().IsProtectedByRMS.

### **Supprime les méthodes obsolètes CellsHelper.DetectLoadFormat() et CellsHelper.DetectFileFormat()**

Utilisez FileFormatUtil.DetectFileFormat() à la place.

### **Supprime la propriété CellsHelper.FontDir obsolète.**

Utilisez plutôt FontConfigs.SetFontsFolder(string, bool).

### **Supprime la propriété CellsHelper.FontDirs obsolète.**

Utilisez plutôt FontConfigs.SetFontFolders(string[], bool).

### **Supprime la propriété CellsHelper.FontFiles obsolète.**

Utilisez plutôt FontConfigs.SetFontSources(FontSourceBase[]).

### **Ajoute la propriété CellsHelper.IsCloudPlatform.**

Indique s'il s'exécute sur la plate-forme pourrait.

### **Ajoute la propriété Shape.Worksheet.**

Obtient la feuille de calcul qui contient cette forme.

### **Ajoute la propriété SaveOptions.SortExternalNames.**

Indique si le tri des noms externes lors de l'enregistrement des fichiers .xlsx.

### **Ajoute la méthode ListObject.Filter().**

Filtre le tableau.

### **Ajoute la méthode XmlMapCollection.Clear().**

Efface toutes les cartes XML.

### **Ajoute l'énumération SaveFormat.Docx.**

Représente cet enregistrement en tant que fichiers .docx.

### **Ajoute l'énumération ImageType.OfficeCompatibleEmf.**

Windows Enhanced Metafile qui est plus compatible avec Office.

