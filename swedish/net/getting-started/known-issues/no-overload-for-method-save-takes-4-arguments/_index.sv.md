---
title: Inga överbelastningar för metoden Spara tar 4 argument
type: docs
weight: 70
url: /sv/net/no-overload-for-method-save-takes-4-arguments/
---

## **Symptom**

"När jag använder Aspose.Cells-versionen får jag detta fel när jag använder Spara-metoden och försöker spara arbetsbok till svarsobjektet. Jag hittar denna kodsnutt dokumenterad i den online-dokumentationen."

### **Skärmbild av felet**

![todo:image_alt_text](no-overload-for-method-save-takes-4-arguments_1.png)

### **Lösning**

Please use **.NET 2.0** compiled version of the product as it works fine on VS.NET 2008/2010. Actually we provide separate dll's for different environments, project types and systems etc. For reference, please check:<https://docs.aspose.com/cells/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/>

Aspose.Cells for .NET är kompatibel och fungerar bra med alla .NET-ramverksversioner dvs. 2.x, 3.x, 4.x etc. för alla typer av projekt t.ex. Asp.NET/Winforms, Webbprojekt, Windows/Webbtjänst, konsolapplikationer eller andra projekt etc. Vi tillhandahåller olika dll:er för olika .NET-ramverksversioner. För mer information, läs filen **readme.txt** i mappen "\Bin" i din installationskatalog. Men, denna **readme.txt**-fil är närvarande.

När du använder vår produkt i en webbapplikation, använd Aspose.Cells.dll från mappen **NET 2.0** i katalogen "/bin". För din information används dll:en i **.NET 3.5 Client Profile**-katalogen endast för konsolapplikationer med Net frame client-profil som målkärnans ramverk för VS.NET. Kontrollera ditt projekt, det är möjligt att ditt projekt refererar till denna dll.

### **Referenser**

<https://forum.aspose.com/t/overload-for-method-save-of-workbook-takes-4-arguments-involving-response-object/121465/1>
