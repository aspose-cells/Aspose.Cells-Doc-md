---
title: TableurML - XLSX, XML
type: docs
weight: 10
url: /fr/net/spreadsheetml-xlsx-xml/
---
## **À propos de SpreadsheetML**
SpreadsheetML est le nom d'une famille de formats XML pour les feuilles de calcul. Il existe plusieurs versions de SpreadsheetML :

1. La version 2003 de SpreadsheetML a été introduite dans Microsoft Word 2003. SpreadsheetML a été une étape importante par Microsoft vers l'ouverture du format de document.
1. [Office XML ouvert](https://en.wikipedia.org/wiki/Office_Open_XML) (OOXML) est le nouveau format XML introduit dans les applications Microsoft Office 2007. Office Open XML est un format de conteneur pour plusieurs langages de balisage spécialisés basés sur XML. SpreadsheetML version 2007 est le langage de balisage utilisé par Microsoft Office Excel 2007 pour stocker ses documents.
1. Microsoft Excel 2010 stocke les documents dans SpreadsheetML version 2010 comme défini dans la norme OOXML mise à jour.
## **TableurML dans Aspose.Cells**
Trois "versions" de SpreadsheetML sont disponibles :

|**SpreadsheetML "Version"**|**Norme/spécification applicables**|**Pris en charge dans Aspose.Cells for .NET**|
|:- |:- |:- |
|Microsoft Excel 2003|[MicrosoftExcel 2003XML](https://en.wikipedia.org/wiki/Microsoft_Office_XML_formats)|Oui|
|Microsoft Excel 2007|[OOXML ECMA-376](https://www.ecma-international.org/publications-and-standards/standards/ecma-376/)|Oui|
|Microsoft Excel 2010|OOXML ISO/IEC DIS 29500|Oui|
|Microsoft Excel 2013|OOXML ISO/IEC DIS 29500|Oui|
Les documents OOXML SpreadsheetML se présentent le plus souvent sous forme de fichiers XLSX, qui sont des packages ZIP. En plus de XLSX. Aspose.Cells fournit une prise en charge étendue pour le chargement, l'enregistrement et la conversion de documents SpreadsheetML. Une telle implémentation globale est possible car Aspose.Cells a été conçu avec la structure des documents Excel Microsoft à l'esprit (et SpreadsheetML est connu pour imiter la représentation interne des documents Excel Microsoft).
### **OOXML est ouvert, pourquoi utiliser Aspose.Cells ?**
Il est vrai que la technologie Office Open XML permet de créer des applications de traitement et de génération de documents en utilisant uniquement les classes XML sans s'appuyer sur des bibliothèques tierces telles que Aspose.Cells. Cependant, nous croyons fermement qu'il est toujours très avantageux d'utiliser Aspose.Cells lorsque vous avez pour traiter des documents OOXML, plutôt que de travailler avec XML ou d'autres bibliothèques.

La spécification OOXML compte plusieurs milliers de pages. Être ouvert et standard ne veut pas dire être simple. Pour traiter ou générer correctement des documents OOXML, il faut investir dans un bon apprentissage du format.

En plus de simplifier le traitement et la génération corrects de documents valides, Aspose.Cells fournit les fonctionnalités importantes suivantes que vous n'auriez pas lorsque vous travaillez avec des fichiers OOXML directement via XML ou d'autres bibliothèques tierces :

- Conversions de qualité entre de nombreux formats Excel populaires, y compris la conversion au format PDF, HTML, TIFF et l'impression.
- Capacité à construire des documents à partir de fragments, à partir d'un ou plusieurs documents, tout en fusionnant automatiquement les données par mise en forme stylistique, tableaux et graphiques.
- Fonctions de haut niveau, telles que l'importation de données à partir de différentes sources de données, notamment Array, ArrayList, DataTable, DataColumn, DataGrid, DataView et DataReader ou l'exportation de données pour remplir un DataTable ou un Array avec une seule ligne de code.
- Moteur de calcul de formule robuste qui prend en charge presque toutes les fonctions Excel standard et avancées Microsoft.

Prenons l'exemple suivant. Certaines cellules contiennent le texte « Hello World » en gras. Imaginez maintenant que vous ayez besoin d'écrire un programme qui recherche toutes les phrases "Hello World" dans la feuille de calcul et les remplace par "Au revoir la Terre".
### **Un fragment d'un document Office Open XML**
**XML**

{{< highlight "csharp" >}}

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


La mise en œuvre même d'une simple opération de recherche et de remplacement dans un document Office Open XML est difficile. Notre conseil : rappelez-vous qu'ouvert et standard ne veut pas dire simple, et utilisez le Aspose.Cells.
