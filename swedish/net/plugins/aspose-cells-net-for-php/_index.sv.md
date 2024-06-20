---
title: Aspose.Cells .NET for PHP
type: docs
weight: 40
url: /sv/net/aspose-cells-net-for-php/
---

## **Komma igång**

### **Introduktion**

### **Systemkrav och stödda plattformar**

#### **Systemkrav**

**Följande är systemkraven för att använda Aspose.Cells .NET för PHP:**

- IIS med installerat PHP och PHP Manager.
- Aspose.Total APIs.
- Aspose.Cells Interop dll- och tlb-filer.

#### **Stödda plattformar**

**Följande plattformar stöds:**

- PHP 5.3 eller senare
- Windows OS

### **Hämta och konfigurera**

#### **Hämta nödvändiga bibliotek**

Ladda ner de nödvändiga biblioteken som nämns nedan. Dessa krävs för att köra exempel på Aspose.Cells Java för PHP.

- [Hämta Aspose.Cells for .NET (DLL eller MSI)-filer från nedladdningsavsnittet](https://downloads.aspose.com/cells/net)
- [Hämta Aspose.Cells for .NET interop dll](https://downloads.aspose.com/cells/net)

Om du laddar ner MSI-versionen, hittar du Aspose.Cells.dll på installationsplatsen vilket är C:\Program Files (x86)\Aspose\Aspose.Cells for .NET\Bin\net2.0-mappen som standard.
Om du har laddat ner DLL-versionen kan du extrahera den och sedan kopiera Aspose.Cells.dll från .NET 2.0-mappen till din c:\temp-mapp för enklare användning.
På liknande sätt, extrahera interop zip-filen och kopiera Aspose.Inteop.dll till c:\temp

#### **Hämta exempel från sociala kodningssajter**

Följande versioner av körande exempel finns tillgängliga att ladda ner på nedan angivna sociala kodningssajter:

-----

##### **GitHub**

- **Aspose.Cells .NET for PHP Examples**

  - [Aspose.Cells .NET for PHP](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

#### **Hur man konfigurerar källkoden på Windows-plattformen**

Följ dessa enkla steg för att öppna och utöka källkoden medan du använder:

##### **1. Registrera både dll- och interop.dll-filer, t.ex. Aspose.Cells.dll och Aspose.Cells.Interop.dll.**

{{< highlight java >}}

 Register both dll and interop.dll files e.g. Aspose.Cells.dll and Aspose.Cells.Interop.dll.

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.dll /codebase

Microsoft (R) .NET Framework Assembly Registration Utility 2.0.50727.7905

Copyright (C) Microsoft Corporation 1998-2004. All rights reserved.

Types registered successfully

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.Interop.dll /codebase

{{< /highlight >}}

##### **2. Aktivera COM- och DOTNET-tillägg i PHP.**

Öppna PHP Manager i IIS och klicka sedan på 'Aktivera för att inaktivera och tillägg'. Hitta php_com_dotnet.dll och se till att det är aktiverat.

##### **3. Konfigurera Aspose.Cells .NET för PHP Exempel**

###### **Metod 1**

Klona PHP exempel från [github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)
och kör följande kommando

{{< highlight java >}}

 composer install

{{< /highlight >}}

###### **Metod 2**

I din PHP-projekts composer.json-fil lägger du till följande rader

{{< highlight java >}}

 {

    "require": {

        "aspose-cells/Aspose.Cells-for-.NET_for_php": "dev-master"

    }

}

{{< /highlight >}}

och kör installera kommandot

{{< highlight java >}}

 composer install

{{< /highlight >}}

To read about composer visit <https://getcomposer.org/>

### **Supporta utvidgning och bidra**

#### **Support**

Från allra första början av Aspose visste vi att det inte bara skulle räcka med att ge våra kunder bra produkter. Vi behövde också leverera en bra service. Vi är själva utvecklare och förstår hur frustrerande det är när en teknisk fråga eller en egenhet i programvaran hindrar dig från att göra det du behöver göra. Vi är här för att lösa problem, inte skapa dem. 

Detta är anledningen till att vi erbjuder kostnadsfri support. Alla som använder våra produkter, vare sig de har köpt dem eller använder en utvärdering, förtjänar vår fulla uppmärksamhet och respekt.

Du kan logga eventuella problem eller förslag som rör Aspose.Cells .NET för PHP via någon av följande plattformar:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

#### **Utvidga och Bidra**

Aspose.Cells .NET for PHP är öppen källkod och dess källkod är tillgänglig på de största sociala kodningswebbplatserna som listas nedan. Utvecklare uppmanas att ladda ner källkoden och bidra genom att föreslå eller lägga till nya funktioner eller förbättra de befintliga, så att andra också kan dra nytta av det.

#### **Källkod**

Du kan få den senaste källkoden från någon av följande platser

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

## **Exempel på kod**

Denna avsnitt inkluderar följande ämnen

- [PHP-programmerarens guide](/cells/sv/net/php-programmers-guide/)
  - [Arbeta med filer i PHP](/cells/sv/net/working-with-files-in-php/)
    - [Filhanteringsfunktioner i PHP](/cells/sv/net/file-handling-features-in-php/)
      - [Öppna filer i PHP](/cells/sv/net/opening-files-in-php/)
      - [Spara filer i PHP](/cells/sv/net/saving-files-in-php/)
    - [Verktygsfunktioner i PHP](/cells/sv/net/utility-features-in-php/)
      - [Kryptering av filer i PHP](/cells/sv/net/encrypting-files-in-php/)
      - [Excel till PDF-omvandling i PHP](/cells/sv/net/excel-to-pdf-conversion-in-php/)
      - [Hantera dokumentegenskaper i PHP](/cells/sv/net/managing-document-properties-in-php/)
      - [Arbetsblads till bild-omvandling i PHP](/cells/sv/net/worksheet-to-image-conversion-in-php/)
  - [Arbeta med formler i PHP](/cells/sv/net/working-with-formulas-in-php/)
    - [Beräkna formler i PHP](/cells/sv/net/calculating-formulas-in-php/)
  - [Arbeta med kalkyler i PHP](/cells/sv/net/working-with-worksheets-in-php/)
    - [Hanteringsfunktioner i PHP](/cells/sv/net/management-features-in-php/)
      - [Hantera arbetsblad i PHP](/cells/sv/net/managing-worksheets-in-php/)
        - [Lägg till arbetsblad i befintlig Excel-fil i PHP](/cells/sv/net/add-worksheets-to-existing-excel-file-in-php/)
        - [Lägg till arbetsblad i ny Excel-fil i PHP](/cells/sv/net/add-worksheets-to-new-excel-file-in-php/)
        - [Ta bort arbetsblad med hjälp av arkindex i PHP](/cells/sv/net/removing-worksheets-using-sheet-index-in-php/)
        - [Ta bort arbetsblad med hjälp av arknamn i PHP](/cells/sv/net/removing-worksheets-using-sheet-name-in-php/)
