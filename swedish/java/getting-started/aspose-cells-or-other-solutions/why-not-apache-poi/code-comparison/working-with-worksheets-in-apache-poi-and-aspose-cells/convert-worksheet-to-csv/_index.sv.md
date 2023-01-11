﻿---
title: Konvertera arbetsblad till CSV
type: docs
weight: 30
url: /sv/java/convert-worksheet-to-csv/
---
## **Aspose.Cells - Konvertera arbetsblad till CSV**
Om utvecklare behöver spara sina filer på någon lagringsplats kan de helt enkelt ange filnamnet (med dess fullständiga lagringssökväg) och önskat filformat (med hjälp av**FileFormatType**uppräkning) medan du anropar**spara**metod av**Arbetsbok**objekt.

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook with Excel file path

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Save the document in PDF format

workbook.save(dataPath + "AsposeWorkbookCSV.csv", SaveFormat.CSV);

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - Konvertera arbetsblad till CSV**
Nedanstående kod visar hur kalkylblad kan konverteras till CSV med Apache POI HSSF och XSSF API jämfört med Aspose.Cells Java API.

**Java**

{{< highlight "java" >}}

 /**

\* En rudimentär XLSX -> CSV processor modellerad på

\* POI-exempelprogram XLS2CSVmra av Nick Burch från

\* paket org.apache.poi.hssf.eventusermodel.examples.

\* Till skillnad från HSSF-versionen ignorerar denna helt

\* saknade rader.

\* <p/>

\* Datablad läses med en SAX-parser för att behålla

\* minnesfotavtryck relativt litet, så detta borde vara

\* kunna läsa enorma arbetsböcker. Stiltabellen och

\* tabellen med delad sträng måste sparas i minnet. De

\* standard tabellklass för POI-stilar används, men en anpassad

\* (skrivskyddad) klass används för den delade strängtabellen

\* eftersom standard POI SharedStringsTable växer mycket

\* snabbt med antalet unika strängar.

\* <p/>

\* Tack till Eric Smith för en patch som åtgärdar ett problem

\* triggas av celler med flera "t"-element, dvs

\* hur Excel representerar olika format (t.ex. ett ord

\* vanligt och ett ord fetstilt).

\*

\* @författare Chris Lott

*/

public class ApacheXLSX2CSV {