---
title: SpreadsheetML - XLSX, XML
type: docs
weight: 10
url: /fr/net/spreadsheetml-xlsx-xml/
---

## **À propos de SpreadsheetML**
SpreadsheetML est un nom pour une famille de formats basés sur XML pour les documents de tableur. Il existe plusieurs versions de SpreadsheetML:

1. La version 2003 de SpreadsheetML a été introduite dans Microsoft Word 2003. SpreadsheetML a été une étape significative par Microsoft vers rendre le format de document ouvert.
1. [Office Open XML](https://en.wikipedia.org/wiki/Office_Open_XML) (OOXML) est le nouveau format basé sur XML introduit dans les applications Microsoft Office 2007. Office Open XML est un format conteneur pour plusieurs langages de balisage basés sur XML spécialisés. La version 2007 de SpreadsheetML est le langage de balisage utilisé par Microsoft Office Excel 2007 pour stocker ses documents.
1. Microsoft Excel 2010 stocke les documents dans la version 2010 de SpreadsheetML telle que définie dans la norme OOXML mise à jour.
## **SpreadsheetML dans Aspose.Cells**
Il existe trois "versions" de SpreadsheetML disponibles:

|**SpreadsheetML "Version"**|**Norme/Spécification Applicable**|**Supporté dans Aspose.Cells for .NET**|
| :- | :- | :- |
|Microsoft Excel 2003|[Microsoft Excel 2003 XML](https://en.wikipedia.org/wiki/Microsoft_Office_XML_formats)|Oui|
|Microsoft Excel 2007|[OOXML ECMA-376](https://www.ecma-international.org/publications-and-standards/standards/ecma-376/)|Oui|
|Microsoft Excel 2010|OOXML ISO/IEC DIS 29500|Oui|
|Microsoft Excel 2013|OOXML ISO/IEC DIS 29500|Oui|
Les documents SpreadsheetML OOXML viennent le plus souvent sous forme de fichiers XLSX, qui sont des packages ZIP. En plus du XLSX, Aspose.Cells offre un soutien étendu pour le chargement, la sauvegarde et la conversion des documents SpreadsheetML. Une telle implémentation globale est possible car Aspose.Cells a été conçu en gardant à l'esprit la structure des documents Microsoft Excel (et SpreadsheetML est connu pour imiter la représentation interne des documents Microsoft Excel).
### **OOXML est Ouvert, Pourquoi Utiliser Aspose.Cells?**
Il est vrai que la technologie Office Open XML permet de construire des applications de traitement de documents et de génération en utilisant uniquement les classes XML sans avoir recours à des bibliothèques tierces telles que Aspose.Cells. Nous croyons cependant fermement qu'il est toujours très bénéfique d'utiliser Aspose.Cells lorsque vous devez travailler avec des documents OOXML, plutôt que de travailler avec XML ou d'autres bibliothèques.

La spécification OOXML fait plusieurs milliers de pages. Être ouvert et standard ne signifie pas être simple. Pour traiter ou générer correctement des documents OOXML, il est nécessaire d'investir dans l'apprentissage du format.

Outre le fait que cela simplifie le traitement et la génération corrects de documents valides, Aspose.Cells offre les fonctionnalités importantes suivantes que vous n'auriez pas en travaillant directement avec des fichiers OOXML via XML ou d'autres bibliothèques tierces:

- Des conversions de qualité entre de nombreux formats populaires d'Excel, y compris la conversion en PDF, HTML, TIFF et l'impression.
- Capacité de construire des documents à partir de fragments, d'un ou de plusieurs documents, tout en fusionnant automatiquement les données par le formatage stylistique, les graphiques et les graphiques.
- Fonctions de haut niveau, telles que l'importation de données à partir de différentes sources de données, y compris Array, ArrayList, DataTable, DataColumn, DataGrid, DataView et DataReader ou l'exportation de données pour remplir un DataTable ou un Array avec juste une ligne de code.
- Moteur de calcul de formule robuste qui prend en charge presque toutes les fonctions standard avancées de Microsoft Excel.

Considérez l'exemple suivant. Certaines cellules contiennent le texte « Hello World » en gras. Maintenant, imaginez que vous devez écrire un programme qui recherche toutes les phrases « Hello World » dans la feuille de calcul et les remplace par « Goodbye Earth ».
### **Un fragment d'un document Office Open XML**
**XML**

{{< highlight csharp >}}

 <?xml version="1.0" encoding="UTF-8" standalone="yes" ?>

\- <worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">

  <dimension ref="A1:M184" />

\- <sheetViews>

\- <sheetView tabSelected="1" workbookViewId="0">

  <selection activeCell="H27" sqref="H27" />

  </sheetView>

  </sheetViews>

  <sheetFormatPr defaultRowHeight="15" />

\- <sheetData>

\- <row r="1" spans="1:7">

\- <c r="A1" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="11" spans="1:7">

\- <c r="D11" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="15" spans="1:7">

\- <c r="G15" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="21" spans="2:7">

\- <c r="G21" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="25" spans="2:7">

\- <c r="F25" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="31" spans="2:7">

\- <c r="B31" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="34" spans="6:13">

\- <c r="M34" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="38" spans="6:13">

\- <c r="F38" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="117" spans="8:8">

\- <c r="H117" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="184" spans="8:8">

\- <c r="H184" s="1" t="s">

  <v>0</v>

  </c>

  </row>

  </sheetData>

  <pageMargins left="0.7" right="0.7" top="0.75" bottom="0.75" header="0.3" footer="0.3" />

</worksheet>



{{< /highlight >}}


Même la mise en œuvre d'une simple opération de recherche et remplacement dans un document Office Open XML est difficile. Notre conseil : rappelez-vous que ouvert et standard ne signifient pas simple, et utilisez Aspose.Cells.
{{< app/cells/assistant language="csharp" >}}
