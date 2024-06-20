# Bibliothèque C++ pour les formats de fichiers Excel

! [Version 23.11.0](https://img.shields.io/badge/nuget-v23.11.0-blue) ! [NuGet](https://img.shields.io/nuget/dt/Aspose.Cells.Cpp)

[![bannière](https://raw.githubusercontent.com/Aspose/aspose.github.io/master/img/banners/aspose_cells-for-cpp-banner.png)](https://releases.aspose.com/cells/cpp/)

[Page du produit](https://products.aspose.com/cells/cpp/) | [Docs](https://docs.aspose.com/cells/cpp/) | [Démos](https://products.aspose.app/cells/family) | [Référence de l'API](https://reference.aspose.com/cells/cpp) | [Exemples](https://github.com/aspose-cells/Aspose.Cells-for-C) | [Blog](https://blog.aspose.com/category/cells/) | [Versions](https://releases.aspose.com/cells/cpp/) | [Support gratuit](https://forum.aspose.com/c/cells) | [Licence temporaire](https://purchase.aspose.com/temporary-license/)

[Aspose.Cells for C++](https://products.aspose.com/cells/cpp/) est une bibliothèque C++ native pour créer, manipuler, traiter et convertir des fichiers Microsoft Excel sans avoir besoin de Microsoft Office ou d'Automatisation. L'API Excel C++ prend en charge Excel 97-2003 (XLS), Excel 2007-2013/2016 (XLSX, XLSM, XLSB), OpenOffice XML et d'autres formats tels que CSV, TSV, et plus encore.

Il permet aux développeurs de travailler avec les lignes, les colonnes, les données, les formules, les tableaux croisés dynamiques, les feuilles de calcul, les tableaux, les graphiques et les objets de dessin à partir de leurs propres applications C++.

## Qu'est-ce que Aspose.Cells for C++?

Aspose.Cells for C++ est une API C++ native sur site permettant d'intégrer les fonctionnalités de création, manipulation et conversion de feuilles de calcul dans vos applications C++. Elle prend en charge le travail avec de nombreux formats de fichier de feuille de calcul populaires de Microsoft Excel (XLS, XLSX, XLSB, CSV, etc.) et OpenOffice/LibreOffice (ODS).

Vous pouvez utiliser Aspose.Cells for C++ pour développer des applications 64 bits dans tout environnement de développement prenant en charge le C++, tel que Microsoft Visual Studio. Aspose.Cells for C++ est un assemblage natif qui peut être déployé en le copiant simplement. Vous n'avez pas à vous soucier des autres services ou modules.

Aspose.Cells for C++ vous permet de travailler avec les propriétés de document intégrées ainsi que les propriétés de document personnalisées dans Microsoft Excel. Prise en charge de la conversion de haute qualité des classeurs Excel en fichiers conformes à PDF/A. Travaillez avec des formules, des tableaux croisés dynamiques, des feuilles de calcul, des tableaux, des plages, des graphiques, des objets OLE et bien plus encore.

## Fonctionnalités de traitement de fichiers Excel

- Ouvrez un fichier de feuille de calcul sans Microsoft Excel.
- [Ouvrez un fichier Excel](https://docs.aspose.com/cells/cpp/different-ways-to-open-files/) via un chemin sur l'ordinateur local ou en utilisant un flux.
- [Convertir la feuille de calcul](https://docs.aspose.com/cells/cpp/converting-worksheet-to-different-image-formats/) dans différents formats d'image.
- [Appliquer une mise en forme conditionnelle](https://docs.aspose.com/cells/cpp/apply-conditional-formatting-in-worksheet/) selon votre choix.
- [Manipuler les tableaux croisés dynamiques](https://docs.aspose.com/cells/cpp/manipulate-pivot-table/) dans vos feuilles de calcul.
- [Convertir un tableau en plage](https://docs.aspose.com/cells/cpp/tables-and-ranges/) sans perdre la mise en forme.
- Consultez le nom d'une cellule en fournissant l'index de ligne et de colonne, de la même manière, [consultez l'index de ligne et de colonne de la cellule](https://docs.aspose.com/cells/cpp/names-and-indices/) d'après son nom.
- Créez un [graphique en pyramide, graphique linéaire, graphique à bulles](https://docs.aspose.com/cells/cpp/creating-and-customizing-charts/), ou un graphique personnalisé.
- [Rendu](https://docs.aspose.com/cells/cpp/chart-rendering/) des types de graphiques pris en charge en images ou en PDF.
- [Insérez un objet OLE dans la feuille de calcul](https://docs.aspose.com/cells/cpp/inserting-ole-objects-into-the-worksheet/).
- Accédez à tous les objets OLE contenus dans la feuille de calcul pour [extraction](https://docs.aspose.com/cells/cpp/extracting-ole-objects-from-worksheet/).

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

Êtes-vous prêt à essayer Aspose.Cells for C++? Exécutez simplement `Install-Package Aspose.Cells.Cpp` depuis la Console du Gestionnaire de package dans Visual Studio pour obtenir le package NuGet. Si vous avez déjà Aspose.Cells for C++ et souhaitez mettre à jour la version, veuillez exécuter `Update-Package Aspose.Cells.Cpp` pour obtenir la dernière version.

### Convertir XLS en XLSX, XLSB & CSV en utilisant C++

Essayez d'exécuter l'extrait ci-dessous pour voir comment fonctionne l'API dans votre environnement ou consultez le [Dépôt GitHub](https://github.com/aspose-cells/Aspose.Cells-for-C) pour d'autres scénarios d'utilisation courants.

```c++
U16String dir(u"your path");
// load the file to be converted
Workbook book(dir + u"template.xls");
// save in different formats
book.Save(dir + u"output.xlsx", SaveFormat::Xlsx);
book.Save(dir + u"output.xlsb", SaveFormat::Xlsb);
book.Save(dir + u"output.csv", SaveFormat::CSV);
book.Save(dir + u"output.json", SaveFormat::Json);
```

### Créer un graphique Excel personnalisé avec C++

```c++
// create a new workbook
Workbook workbook;

// get first worksheet which is created by default
Worksheet worksheet = workbook.GetWorksheets().Get(0);

// add sample data
worksheet.GetCells().Get(u"A1").PutValue(50);
worksheet.GetCells().Get(u"A2").PutValue(100);
worksheet.GetCells().Get(u"A3").PutValue(150);
worksheet.GetCells().Get(u"A4").PutValue(110);
worksheet.GetCells().Get(u"B1").PutValue(260);
worksheet.GetCells().Get(u"B2").PutValue(12);
worksheet.GetCells().Get(u"B3").PutValue(50);
worksheet.GetCells().Get(u"B4").PutValue(100);

// add a chart to the worksheet
int chartIndex = worksheet.GetCharts().Add(Aspose::Cells::Charts::ChartType::Column, 5, 0, 20, 8);

// access the instance of the newly added chart
Chart chart = worksheet.GetCharts().Get(chartIndex);

// add SeriesCollection (chart data source) to the chart ranging from A1 to B4
chart.GetNSeries().Add(u"A1:B4", true);

// set the chart type of 2nd NSeries to display as line chart
chart.GetNSeries().Get(1).SetType(
	Aspose::Cells::Charts::ChartType::Line);

// save the Excel file
workbook.Save(u"output.xlsx");
```

[Page du produit](https://products.aspose.com/cells/cpp/) | [Docs](https://docs.aspose.com/cells/cpp/) | [Démos](https://products.aspose.app/cells/family) | [Référence de l'API](https://reference.aspose.com/cells/cpp) | [Exemples](https://github.com/aspose-cells/Aspose.Cells-for-C) | [Blog](https://blog.aspose.com/category/cells/) | [Versions](https://releases.aspose.com/cells/cpp/) | [Support gratuit](https://forum.aspose.com/c/cells) | [Licence temporaire](https://purchase.aspose.com/temporary-license/)
