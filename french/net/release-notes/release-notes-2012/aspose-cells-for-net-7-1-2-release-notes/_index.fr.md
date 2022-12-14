---
title: Aspose.Cells for .NET 7.1.2 Notes de mise à jour
type: docs
weight: 90
url: /fr/net/aspose-cells-for-net-7-1-2-release-notes/
---
{{% alert color="primary" %}} 

 Cette page contient des notes de version pour[Aspose.Cells for .NET 7.1.2](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-7.1.2/)

{{% /alert %}} 

Nous sommes heureux d'annoncer Aspose.Cells for .NET v7.1.2!1) Aspose.Cells

 Nouvelles fonctionnalités

 ` `- Support Tables in XLS files - Customizing the Ribbon XML40452 - Support Workbook.ContentTypePropertiesEnhancements

 ` `- La formule IF() renvoie "0" au lieu de "#N/A" - Problèmes avec la propriété FirstPageNumber - La mise en page a été modifiée lors de la conversion du document en PDF - La propriété 'DragData' est manquante dans 'PivotField' - Modifier la source de données sur le tableau croisé dynamique . - Problèmes avec les tableaux croisés dynamiques - Convertir le diagramme/les formes de flux de travail en image(s)

 ` `- Worksheet.RemoveFormulas - problème de performances - Génération Pdf => OutOfMemoryException - Utilisation excessive de la mémoire lors de la conversion d'Excel en PDF - L'enregistrement au format PDF utilise 3 Go pour un fichier Excel de 10 Mo - L'ouverture du classeur prend trop de temps pour ouvrir les exceptions

` ` - Exception NullReference lors de l'opération d'enregistrement en cas de copie d'une feuille de calcul à partir d'un autre classeur - Crash sur la méthode Workbook.CalculateFormula() - L'attribut RowSpan lève une exception - Une exception ArgumentOutOfRangeException s'est produite lors de l'initialisation du fileBugs

` `- Problèmes de fonctions VLOOKUP et OFFSET - IRR n'est pas calculé correctement - Problèmes de calculs MS Excel - La formule matricielle utilisant la fonction Indirect() ne copie qu'une seule valeur - CellsException dans le calcul de la formule TREND() - Copier la feuille de calcul remplace l'en-tête et le pied de page - Problème d'impression Excel fichier avec des images EMF intégrées - Problème de tableau croisé dynamique - Bogue de filtre de formatage - PivotField - Lecture d'éléments à partir du cache - Plusieurs problèmes lors de la mise à niveau vers les dernières versions - La création d'un classeur avec InputStream ne fonctionne pas - Le fichier XLS généré plante MS Excel - La liste déroulante et le graphique sont supprimé du classeur après l'enregistrement - Aspose.Cells n'applique pas correctement le formatage de cellule personnalisé - Les fichiers XLSM sont corrompus dans certaines conditions - Le format de taille de police Cell avec un nombre non entier a changé - Insérer un symbole à la fin d'une valeur de cellule2) GridDesktop

 Insectes

` ` - Les valeurs de graphique sont affichées à tort pour le fichier XLSX - Problème SUM () dans la feuille de calcul de GridDesktop - GridDesktop.ImportExcelFile () génère une exception - L'index était en dehors des limites du tableau - Problème de GridDestop sur les cellules de formule - Griddesktop.ImportExcelFile () lève l'exception OutOfMemory
