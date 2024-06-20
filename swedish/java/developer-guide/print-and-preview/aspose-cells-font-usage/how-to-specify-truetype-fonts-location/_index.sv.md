---
title: Hur man anger plats för TrueType typsnitt
type: docs
weight: 30
url: /sv/java/how-to-specify-truetype-fonts-location/
---

{{% alert color="primary" %}}

Den här artikeln beskriver:

1. [Var Aspose.Cells API letar efter TrueType-typsnitt](/cells/sv/java/how-to-specify-truetype-fonts-location/#where-asposecells-looks-for-truetype-fonts-on-windows).
1. [Hur man explicit anger en mapp för TrueType-typsnitt för Aspose.Cells API](/cells/sv/java/how-to-specify-truetype-fonts-location/#how-to-explicitly-specify-a-font-folder).
1. [Hur man begränsar Aspose.Cells API att använda bara en plats för TrueType-typsnitt](/cells/sv/java/how-to-specify-truetype-fonts-location/#how-to-restrict-the-asposecells-to-use-only-one-font-folder).

{{% /alert %}}

## **Arbeta med typsnitt**

### **Var Aspose.Cells Letar efter TrueType-typsnitt på Windows**

Aspose.Cells letar efter teckensnitt i mappen **Windows \ Fonts**. Denna standardinställning fungerar mest hela tiden så ange bara dina egna teckensnittsmappar om du verkligen behöver det.

### **Var Aspose.Cells letar efter TrueType-teckensnitt på Linux**

Som standard letar Aspose.Cells API efter teckensnitt i alla följande platser, även om olika Linux-distributioner lagrar teckensnitt i olika mappar.

1. /usr/share/fonts
1. /usr/local/share/fonts

{{% alert color="primary" %}}

Denna standardinställning fungerar för de flesta Linux-distributioner, men det är inte garanterat att det fungerar hela tiden. Du kan behöva specificera platsen för TrueType-teckensnitten explicit. 

{{% /alert %}}

### **Hur man explicit specifierar en mapp för teckensnitt**

Aspose.Cells API: er har utsatt många fabriksmetoder för klassen FontConfigs för att ange teckensnitten eller teckensnittets mappar som beskrivs nedan.

1. setFontFolder-metoden accepterar första parametern av typen String med plats till teckensnittskatalogen medan den andra parametern av typen Boolean riktar Aspose.Cells APis att söka mapparna rekursivt för filer med teckensnitt.
1. setFontFolders-metoden accepterar en array av typen String så du kan ange många teckensnittskataloger med den här metoden. Du kan också dirigera Aspose.Cells APis att söka mapparna rekursivt genom att ange true som andra parameter.
1. setFontSources-metoden accepterar en array av typen FontSourceBase för att du ska kunna ange en lista över enskilda teckensnittsplatser.

{{% alert color="primary" %}}

När du specifierar teckensnittsmappen med någon av de ovan nämnda metoderna rekommenderar vi att du anger teckensnittsplatsen i början av applikationen annars kan du få dåligt formatterade resultat.

{{% /alert %}} {{% alert color="primary" %}}

Att ange teckensnittsmappen med någon av de ovanstående metoderna garanterar inte att Aspose.Cells API inte kommer att leta efter teckensnitten på standardplatser som systemets teckensnittsmapp.

{{% /alert %}}

### **Hur du begränsar Aspose.Cells att använda bara en teckensnittsmapp**

Från och med Aspose.Cells for Java 8.1.0 säkerställer inställningen av JVM-argument som **-DAspose.Cells.FontDirExc = "DinFontDir** att Aspose.Cells API bara kommer att använda teckensnittsplatsen som specificerats.

Ställ in de angivna argumenten med System.setProperty-metoden som visas nedan.

{{< highlight java >}}

System.setProperty("Aspose.Cells.FontDirExc", "FontDirSet");

{{< /highlight >}}

{{% alert color="primary" %}}

Observera följande:

- Ovanstående uttalande bör vara i början av din applikation.
- Genom att använda ovanstående tillvägagångssätt krävs inte att fontkatalogen ställs in med någon av de FontConfigs-metoder som diskuteras ovan.
- Strängen "FontDirSet" bör vara den kompletta sökvägen till mappen som innehåller de nödvändiga teckensnitten.

{{% /alert %}}
