---
title: Hur installerar man typsnitt i Linux
type: docs
description: "Hur installerar man typsnitt i Linux"
weight: 139
url: /sv/net/how-to-install-font-in-linux/
---

## Översikt

När du använder Aspose.Cells i Linux, eftersom Linux har färre standardtypsnitt, kanske det typsnitt som hänvisas till i din Excel-fil inte finns som standard på ditt Linux-system.
När detta händer, kommer Aspose.Cells istället att använda ett liknande typsnitt för att visa tecknen. Detta kan dock orsaka följande effekter:

1. Olika typsnitt kan resultera i att bilder renderas i andra layouter än i Excel.
2. Eftersom typsnittet har ändrats kanske output-tecknen inte blir som du önskar.

För att ditt program ska kunna ge mer exakta resultat, installera de typsnitt du behöver under Linux. Det är viktigt att se till att de typsnitt du använder i Excel-filer finns i din miljö.

## Hur installerar man typsnitt i Linux

Det finns två sätt att installera teckensnitt på Linux, som beskrivs nedan:

### Kopiera fontfiler till Linux-systemvägen

1. Sätt en mapp med namnet "fonts" i din programkatalog, kopiera de fontfiler du behöver till denna mapp.
2. Lägg till följande kommando i din Linux Dockerfile:
```
COPY fonts/ /usr/share/fonts
```
3. Efter ovanstående operation kommer fontfilerna att kopieras till Linux-systemvägen. Aspose.Cells kommer att gå till systemvägen för att hitta och använda dem. Detta är vårt rekommenderade scenario.

### Ställ in Font-mappen med Aspose.Cells API
I vissa fall kan det hända att du inte kan kontrollera eller ändra Linux-systemkatalogen. Till exempel på molnservrar. I detta fall kan du använda det andra scenariot.
1. Sätt en mapp med namnet "fonts" i din programkatalog och kopiera de fontfiler du behöver till denna mapp.
2. Anropa Aspose.Cells API i din programkod:
```
Aspose.Cells.FontConfigs.SetFontFolder("fonts", true);
```
3. Ovanstående operation säkerställer att programmet kan hitta fonten från projektvägen.

## Se även

- [Hur man kör Aspose.Cells för .Net6](https://docs.aspose.com/cells/net/how-to-run-aspose-cells-for-net6/)

{{< app/cells/assistant language="csharp" >}}
