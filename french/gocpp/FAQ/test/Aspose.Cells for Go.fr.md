# Bibliothèque Go pour les formats de fichiers Excel

![Version 24.11.0](https://img.shields.io/badge/go-v24.11.0-blue)

[Page Produit](https://products.aspose.com/cells/go-cpp/) | [Docs](https://docs.aspose.com/cells/go-cpp/) | [Démos](https://products.aspose.app/cells/family) | [Référence API](https://reference.aspose.com/cells/go-cpp) | [Exemples](https://github.com/aspose-cells/aspose-cells-go-cpp) | [Blog](https://blog.aspose.com/category/cells/) | [Versions](https://releases.aspose.com/cells/go-cpp/) | [Support Gratuit](https://forum.aspose.com/c/cells) | [Licence Temporaire](https://purchase.aspose.com/temporary-license/)

[Aspose.Cells for Go via C++](https://products.aspose.com/cells/go-cpp/) est une bibliothèque Go native pour créer, manipuler, traiter et convertir des fichiers Microsoft Excel sans nécessiter Microsoft Office ou l'automatisation. L'API Excel pour Go supporte Excel 97-2003 (XLS), Excel 2007-2013/2016 (XLSX, XLSM, XLSB), OpenOffice XML, et d'autres formats comme CSV, TSV, et plus.

Il permet aux développeurs de travailler avec les lignes, colonnes, données, formules, tableaux croisés dynamiques, feuilles de calcul, tables, graphiques et objets de dessin de leurs propres applications Go.

## Qu'est-ce que Aspose.Cells for Go via C++ ?

Aspose.Cells for Go via C++ est une API native Go sur site pour intégrer des fonctionnalités de création, manipulation et conversion de feuilles de calcul dans vos applications Go. Elle supporte de nombreux formats de fichiers de feuilles de calcul populaires de Microsoft Excel (XLS, XLSX, XLSB, CSV, etc.) et OpenOffice/LibreOffice (ODS).

Vous pouvez utiliser Aspose.Cells for Go via C++ pour développer des applications 64 bits dans n'importe quel environnement de développement supportant Go, comme Microsoft Visual Studio. Aspose.Cells for Go via C++ est un assemblage natif qui peut être déployé simplement en le copiant. Vous n'avez pas à vous soucier des autres services ou modules.

Aspose.Cells for Go via C++ vous permet de travailler avec les propriétés du document intégrées ainsi que personnalisées dans Microsoft Excel. Supporte une conversion de haute qualité des classeurs Excel en fichiers conformes PDF/A. Travaillez avec des formules, tableaux croisés dynamiques, feuilles, tableaux, plages, graphiques, objets OLE et bien plus encore.

## Fonctionnalités de traitement de fichiers Excel

- Ouvrez un fichier de feuille de calcul sans Microsoft Excel.
- [Ouvrir un fichier Excel](https://docs.aspose.com/cells/go/different-ways-to-open-files/) via un chemin sur l'ordinateur local ou en utilisant un flux.
- [Convertir une feuille de calcul](https://docs.aspose.com/cells/go/converting-worksheet-to-different-image-formats/) en différents formats d'image.
- [Appliquer une mise en forme conditionnelle](https://docs.aspose.com/cells/go/apply-conditional-formatting-in-worksheet/) selon votre choix.
- [Manipuler les tableaux croisés dynamiques](https://docs.aspose.com/cells/go/manipulate-pivot-table/) dans vos feuilles de calcul.
- [Convertir un tableau en plage](https://docs.aspose.com/cells/go/tables-and-ranges/) sans perdre la mise en forme.
- Récupérer le nom d'une cellule en fournissant l'indice de ligne et de colonne, de même, [récupérer l'indice de ligne et de colonne de la cellule](https://docs.aspose.com/cells/go/names-and-indices/) depuis son nom.
- Créer un [graphique en pyramide, un graphique en ligne, un graphique à bulles](https://docs.aspose.com/cells/go/creating-and-customizing-charts/) ou un graphique personnalisé.
- [Rendu](https://docs.aspose.com/cells/go/chart-rendering/) des types de graphiques supportés en images ou PDF.
- [Insérer un objet OLE dans la feuille](https://docs.aspose.com/cells/go/inserting-ole-objects-into-the-worksheet/).
- Accéder à tous les objets OLE contenus dans la feuille pour [extraction](https://docs.aspose.com/cells/go/extracting-ole-objects-from-worksheet/).

## Formats de lecture et d'écriture pris en charge

**Microsoft Excel:** XLS, XLSX, XLSB, SpreadsheetML\
**Text:** CSV, TSV, TabDelimited\
**OpenDocument:** ODS\
**Autre :** HTML, MHTML

## Enregistrer les documents de feuille de calcul sous

**Microsoft Excel:** XLSM, XLTX, XLTM, XLAM\
**Format de document portable :** PDF, XPS\
**Text:** CSV, TSV, TabDelimited\
**Images :** SVG, JPEG, PNG, BMP, GIF
**Web:** HTML, MHTML\
**Métafichier:** EMF\
**Autre** DIF

## Commencer

Prêt à essayer Aspose.Cells for Go via C++ ? Exécutez simplement `go get -u github.com/aspose-cells/aspose-cells-go-cpp` et importez `github.com/aspose-cells/aspose-cells-go-cpp` dans votre fichier Go. Si vous avez déjà Aspose.Cells for Go via C++ et souhaitez mettre à jour la version, exécutez `go get github.com/aspose-cells/aspose-cells-go-cpp@v24.12.0` pour obtenir la dernière version.

### Convertir XLS en XLSX, XLSB & CSV en utilisant Go

Essayez d'exécuter le code ci-dessous pour voir comment l'API fonctionne dans votre environnement ou consultez le [dépôt GitHub](https://github.com/aspose-cells/aspose-cells-go-cpp) pour d'autres scénarios d'utilisation courants.

```Go
lic, _ := NewLicense()
lic.SetLicense_String(os.Getenv("LicensePath"))
workbook, err1 := NewWorkbook_String("Book1.xlsx")
if err1 != nil {
    println(err1)
}
workbook.Save_String("Book1.pdf")
workbook.Save_String("Book1.png")
workbook.Save_String("Book1.txt")
workbook.Save_String("Book1.ods")
workbook.Save_String("Book1.md")
workbook.Save_String("Book1.json")
workbook.Save_String("Book1.html")
```

### Créer un graphique Excel personnalisé avec Go

```Go
package main

import (
 . "asposecells"
 "os"
)

func main() {
 lic, _ := NewLicense()
 lic.SetLicense_String(os.Getenv("LicensePath"))

 workbook, _ := NewWorkbook()
 worksheets, _ := workbook.GetWorksheets()
 worksheet, _ := worksheets.Get_Int(0)
 cells, _ := worksheet.GetCells()
 cell, _ := cells.Get_String("A1")
 cell.PutValue_Int(50)
 cell, _ = cells.Get_String("A2")
 cell.PutValue_Int(100)
 cell, _ = cells.Get_String("A3")
 cell.PutValue_Int(150)
 cell, _ = cells.Get_String("B1")
 cell.PutValue_Int(4)
 cell, _ = cells.Get_String("B2")
 cell.PutValue_Int(20)
 cell, _ = cells.Get_String("B3")
 cell.PutValue_Int(50)
 charts, _ := worksheet.GetCharts()
 chartIndex, _ := charts.Add_ChartType_Int_Int_Int_Int(ChartType_Pyramid, 5, 0, 20, 8)
 chart, _ := charts.Get_Int(chartIndex)
 series, _ := chart.GetNSeries()
 series.Add_String_Bool("A1:B3", true)
 workbook.Save_String("CreateChart.xlsx")
}

```

[Page Produit](https://products.aspose.com/cells/go-cpp/) | [Docs](https://docs.aspose.com/cells/go-cpp/) | [Démos](https://products.aspose.app/cells/family) | [Référence API](https://reference.aspose.com/cells/go-cpp) | [Exemples](https://github.com/aspose-cells/aspose-cells-go-cpp) | [Blog](https://blog.aspose.com/category/cells/) | [Versions](https://releases.aspose.com/cells/go-cpp/) | [Support Gratuit](https://forum.aspose.com/c/cells) | [Licence Temporaire](https://purchase.aspose.com/temporary-license/)
