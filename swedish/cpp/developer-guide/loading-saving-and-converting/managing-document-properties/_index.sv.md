---
title: Hantera dokumentegenskaper
type: docs
weight: 30
url: /sv/cpp/managing-document-properties/
---

## **Möjliga användningsscenarier**
Aspose.Cells gör att du kan arbeta med inbyggda och anpassade dokumentegenskaper. Här är Microsoft Excel-gränssnittet för att öppna dessa * Dokumentegenskaper *. Klicka helt enkelt på * Avancerade egenskaper *, som visas i den här skärmdumpen och visa dem.

![todo:image_alt_text](managing-document-properties_1.png)
## **Hantera dokumentegenskaper**
Följande exempelkod laddar [provexelfil](23166989.xlsx) och läser inbyggda dokumentegenskaper, till exempel * Titel, Ämne * och ändrar dem sedan. Sedan läser den också in anpassad dokumentegenskap dvs * MyCustom1 * och lägger till en ny anpassad dokumentegenskap dvs * MyCustom5 * och skriver [utmatningsexfil](23166986.xlsx). Följande skärmdump visar effekten av exempelkoden på provexelfilen.

![todo:image_alt_text](managing-document-properties_2.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-ManagingDocumentProperties-new.cpp" >}}


## **Konsoloutput**
Det här är konsoloutputen från ovanstående exempelkod när den körs med den tillhandahållna [provexelfilen](23166989.xlsx).

{{< highlight java >}}

 Title: Aspose Team

Subject: Aspose.Cells for C++

MyCustom1: This is my custom one.

{{< /highlight >}}
