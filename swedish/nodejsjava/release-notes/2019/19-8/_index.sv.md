---
title: Aspose.Cells för Node.js via Java 19.8 Release Notes
type: docs
weight: 10
url: /sv/nodejs-java/aspose-cells-for-node-js-via-java-19-8-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells för Node.js via Java 19.8.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42861|Det gick inte att hämta formens alternativa text i ODS-filformat|Insekt|
|CELLSJAVA-42929|Graftiteländringar vid konvertering av XLSX till PDF|Insekt|
|CELLSJAVA-42933|Grafikens färg ändras när Excel-filen konverteras till PDF|Insekt|
|CELLSJAVA-42946|Fel rendering av staplade stapeldiagram med serier till PDF|Insekt|
|CELLSJAVA-42942|Sidor som skrivs ut på kalkylbladsnivå och inte på arbetsboksnivå|Insekt|
|CELLSJAVA-42952|Fel indrag från toppen av cellen i vissa ord|Insekt|
|CELLSJAVA-42902|Vattenfallsdiagramsstil kopieras inte korrekt när arbetsboken kopieras|Insekt|
|CELLSJAVA-42939|Varning väckt av Excel om vi bara kallar Workbook.getVbaProject() för en arbetsbok|Insekt|
|CELLSJAVA-42940|Säkerhetsvarning efter borttagning av alla VBA-modulskript|Insekt|
|CELLSJAVA-42955|Att öppna VBAProject förstör arbetsboken|Insekt|
|CELLSJAVA-42945|Spara som HTML kastar undantag om ExportImagesAsBase64 är inställt|Undantag|
|CELLSJAVA-42953|NullPointerException vid konvertering av XLS-filer till HTML|Undantag|
|CELLSJAVA-42951|java.lang.NullPointerException slängt av comment.setHtmlNote()|Undantag|
|CELLSJAVA-42954|Undantag uppstod när XLSX-filen laddades och sparades|Undantag|
|CELLSJAVA-42957|Ogiltigt FontUnderlineType-värde kastas när XLSX-fil sparas|Undantag|
### **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells för Node.js via Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
#### **Uppgraderar det refererade BouncyCastle-biblioteket till 1.60**
Det bifogade BouncyCastle-biblioteket i releasearkivet har uppgraderats till version 1.60. Men Aspose.Cells är kompatibel med gamla versioner också, så användaren kan fortfarande använda de gamla versionerna som 1.46.
#### **Föråldrar HTMLLoadOptions-klassen och lägger till HtmlLoadOptions-klassen**
Använd klassen HtmlLoadOptions istället.
#### **Föråldrar klassen ODSLoadOptions och lägger till klassen OdsLoadOptions**
Använd klassen OdsLoadOptions istället.
#### **Föråldrar JSONUtility-klassen och lägger till JsonUtility-klassen**
Använd klassen JsonUtility istället.
#### **Lägger till gränssnitt IPageSavingCallback**
Kontrollera/indikera framsteg för sidsparprocessen.
#### **Lägger till klass PageSavingArgs**
Info för en process för att spara sidan.
#### **Lägger till klass PageStartSavingArgs**
Info för en sida startar sparningsprocessen.
#### **Lägger till klass PageEndSavingArgs**
Info för en sida avslutar sparprocessen.
#### **Lägger till egenskapen PdfSaveOptions.PageSavingCallback**
Kontrollera/indikera framsteg för sidsparprocessen.

