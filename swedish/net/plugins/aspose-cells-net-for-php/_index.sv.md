---
title: Aspose.Cells .NET for PHP
type: docs
weight: 40
url: /sv/net/aspose-cells-net-for-php/
---
## **Komma igång**

### **Introduktion**

### **Systemkrav och plattformar som stöds**

#### **Systemkrav**

**Följande är systemkraven för att använda Aspose.Cells .NET for PHP:**

- IIS med PHP och PHP Manager installerat.
- Aspose.Total API:er.
- Aspose.Cells Interop dll- och tlb-filen.

#### **Plattformar som stöds**

**Följande är de plattformar som stöds:**

- PHP 5.3 eller högre
- Windows OS

### **Ladda ner och konfigurera**

#### **Ladda ner obligatoriska bibliotek**

Ladda ner nödvändiga bibliotek som nämns nedan. Dessa är nödvändiga för att exekvera Aspose.Cells Java for PHP exempel.

- [Ladda ner Aspose.Cells for .NET (DLL eller MSI) filer från nedladdningssektionen](https://downloads.aspose.com/cells/net)
- [Ladda ner Aspose.Cells for .NET interop dll](https://downloads.aspose.com/cells/net)

Om du laddar ner MSI-versionen hittar du Aspose.Cells.dll på den installerade platsen som är mappen C:\Program Files (x86)\Aspose\Aspose.Cells Aspose.Cells for .NET\Bin\net2.0 som standard.
Men om du har laddat ner DLL-versionen kan du extrahera den och sedan kopiera Aspose.Cells.dll från .NET 2.0-mappen till din c:\temp-mapp för enkel användning.
Extrahera på liknande sätt interop zip-fil och kopiera Aspose.Inteop.dll till c:\temp

#### **Ladda ner exempel från webbplatser för social kodning**

Följande versioner av löpande exempel finns att ladda ner på nedan nämnda webbplatser för social kodning:

-----

##### **GitHub**

- **Aspose.Cells .NET for PHP Exempel**

  - [Aspose.Cells .NET for PHP](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

#### **Hur man konfigurerar källkoden på Windows-plattformen**

Följ dessa enkla steg för att öppna och utöka källkoden medan du använder:

##### **1. Registrera både dll- och interop.dll-filer, t.ex. Aspose.Cells.dll och Aspose.Cells.Interop.dll.**

{{< highlight "java" >}}

 Register both dll and interop.dll files e.g. Aspose.Cells.dll and Aspose.Cells.Interop.dll.

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.dll /codebase

Microsoft (R) .NET Framework Assembly Registration Utility 2.0.50727.7905

Copyright (C) Microsoft Corporation 1998-2004. All rights reserved.

Types registered successfully

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.Interop.dll /codebase

{{< /highlight >}}

##### **2. Aktivera COM- och DOTNET-tillägg i PHP.**

Öppna PHP Manager i IIS och klicka sedan på "Aktivera för att inaktivera och tillägg". Hitta php_com_dotnet.dll och se till att den är aktiverad.

##### **3. Konfigurera Aspose.Cells .NET for PHP Exempel**

###### **Metod 1**

 Klona PHP exempel från[github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)
och kör följande kommando

{{< highlight "java" >}}

 composer install

{{< /highlight >}}

###### **Metod 2**

Lägg till följande rader i ditt PHP-projekts composer.json-fil

{{< highlight "java" >}}

 {

    "require": {

        "aspose-cells/Aspose.Cells-for-.NET_for_php": "dev-master"

    }

}

{{< /highlight >}}

och kör installationskommandot

{{< highlight "java" >}}

 composer install

{{< /highlight >}}

 Att läsa om kompositörsbesök<https://getcomposer.org/>

### **Support Utöka och bidra**

#### **Stöd**

Från de allra första dagarna av Aspose visste vi att det inte skulle räcka att bara ge våra kunder bra produkter. Vi behövde också leverera bra service. Vi är själva utvecklare och förstår hur frustrerande det är när ett tekniskt problem eller en egenhet i programvaran hindrar dig från att göra det du behöver göra. Vi är här för att lösa problem, inte skapa dem.

Det är därför vi erbjuder gratis support. Alla som använder vår produkt, oavsett om de har köpt dem eller använder en utvärdering, förtjänar vår fulla uppmärksamhet och respekt.

Du kan logga alla problem eller förslag relaterade till Aspose.Cells .NET for PHP med någon av följande plattformar:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

#### **Utöka och bidra**

Aspose.Cells .NET for PHP är öppen källkod och dess källkod är tillgänglig på de stora sociala kodningswebbplatserna nedan. Utvecklare uppmuntras att ladda ner källkoden och bidra genom att föreslå eller lägga till nya funktioner eller förbättra de befintliga, så att andra också kan dra nytta av den.

#### **Källkod**

Du kan få den senaste källkoden från en av följande platser

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

## **Exempel på kodexempel**

Det här avsnittet innehåller följande ämnen

- [PHP programmerare guide](/cells/sv/net/php-programmers-guide/)
  - [Arbeta med filer i PHP](/cells/sv/net/working-with-files-in-php/)
    - [Filhanteringsfunktioner i PHP](/cells/sv/net/file-handling-features-in-php/)
      - [Öppna filer i PHP](/cells/sv/net/opening-files-in-php/)
      - [Spara filer i PHP](/cells/sv/net/saving-files-in-php/)
    - [Verktygsfunktioner i PHP](/cells/sv/net/utility-features-in-php/)
      - [Kryptera filer i PHP](/cells/sv/net/encrypting-files-in-php/)
      - [Excel till PDF Konvertering i PHP](/cells/sv/net/excel-to-pdf-conversion-in-php/)
      - [Hantera dokumentegenskaper i PHP](/cells/sv/net/managing-document-properties-in-php/)
      - [Arbetsblad till bildkonvertering i PHP](/cells/sv/net/worksheet-to-image-conversion-in-php/)
  - [Arbeta med formler i PHP](/cells/sv/net/working-with-formulas-in-php/)
    - [Beräkna formler i PHP](/cells/sv/net/calculating-formulas-in-php/)
  - [Arbeta med kalkylblad i PHP](/cells/sv/net/working-with-worksheets-in-php/)
    - [Hanteringsfunktioner i PHP](/cells/sv/net/management-features-in-php/)
      - [Hantera arbetsblad i PHP](/cells/sv/net/managing-worksheets-in-php/)
        - [Lägg till kalkylblad till befintlig Excel-fil i PHP](/cells/sv/net/add-worksheets-to-existing-excel-file-in-php/)
        - [Lägg till kalkylblad till ny Excel-fil i PHP](/cells/sv/net/add-worksheets-to-new-excel-file-in-php/)
        - [Ta bort arbetsblad med Sheet Index i PHP](/cells/sv/net/removing-worksheets-using-sheet-index-in-php/)
        - [Ta bort arbetsblad med Sheet Name i PHP](/cells/sv/net/removing-worksheets-using-sheet-name-in-php/)
