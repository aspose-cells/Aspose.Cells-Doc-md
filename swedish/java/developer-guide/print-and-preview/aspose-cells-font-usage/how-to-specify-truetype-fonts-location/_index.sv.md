---
title: Så här anger du TrueType-teckensnittsplats
type: docs
weight: 30
url: /sv/java/how-to-specify-truetype-fonts-location/
---
{{% alert color="primary" %}}

Den här artikeln beskriver:

1. [Där Aspose.Cells API letar efter TrueType-teckensnitt](/cells/sv/java/how-to-specify-truetype-fonts-location/#where-asposecells-looks-for-truetype-fonts-on-windows).
1. [Hur man uttryckligen anger en TrueType-teckensnittsmapp för Aspose.Cells API](/cells/sv/java/how-to-specify-truetype-fonts-location/#how-to-explicitly-specify-a-font-folder).
1. [Så här begränsar du Aspose.Cells API till att endast använda en plats för TrueType-teckensnitt](/cells/sv/java/how-to-specify-truetype-fonts-location/#how-to-restrict-the-asposecells-to-use-only-one-font-folder).

{{% /alert %}}

## **Arbeta med teckensnitt**

### **Där Aspose.Cells letar efter TrueType-teckensnitt på Windows**

 Aspose.Cells söker efter teckensnitt i**Windows\Teckensnitt** mapp. Den här standardinställningen fungerar för det mesta så ange bara dina egna teckensnittsmappar om du verkligen behöver det.

### **Där Aspose.Cells letar efter TrueType-teckensnitt på Linux**

Som standard letar Aspose.Cells API efter teckensnitten på alla följande platser, även om olika Linux-distributioner lagrar teckensnitt i olika mappar.

1. /usr/share/fonts
1. /usr/local/share/fonts

{{% alert color="primary" %}}

 Detta standardbeteende kommer att fungera för de flesta Linux-distributioner, men det är inte garanterat att det fungerar hela tiden. Du kan behöva ange platsen för TrueType-teckensnitten uttryckligen.

{{% /alert %}}

### **Hur man explicit anger en typsnittsmapp**

Aspose.Cells API:er har avslöjat många fabriksmetoder för FontConfigs-klassen för att specificera typsnitt eller typsnittsmappar enligt beskrivningen nedan.

1. Metoden setFontFolder accepterar den första parametern av typen String med plats till teckensnittskatalogen medan den andra parametern av typen Boolean är att styra AP:erna Aspose.Cells att söka i mapparna rekursivt efter teckensnittsfiler.
1. Metoden setFontFolders accepterar en array av typen String så att du kan ange många teckensnittskataloger med detta tillvägagångssätt. Du kan också be AP:erna Aspose.Cells att söka i mapparna rekursivt genom att ange true som andra parameter.
1. Metoden setFontSources accepterar en array av typen FontSourceBase så att du kan ange en lista över individuella teckensnitts placeringar.

{{% alert color="primary" %}}

När du anger teckensnittsmappen med någon av de ovan nämnda metoderna rekommenderar vi att du ställer in teckensnittsplatsen i början av programmet, annars kan du få dåligt formaterade resultat.

{{% /alert %}} {{% alert color="primary" %}}

Att ställa in teckensnittsmappen med någon av ovanstående metoder säkerställer inte att Aspose.Cells API inte letar efter teckensnitten på standardplatser som systemets teckensnittsmapp.

{{% /alert %}}

### **Hur man begränsar Aspose.Cells till att endast använda en typsnittsmapp**

 Med start från Aspose.Cells for Java 8.1.0, ställ in JVM-argumenten som**-DAspose.Cells.FontDirExc="Din teckensnittskatalog**kommer att se till att Aspose.Cells API endast kommer att använda teckensnittsplatsen som specificerats.

Ställ in de angivna argumenten med metoden System.setProperty som visas nedan.

{{< highlight "java" >}}

System.setProperty("Aspose.Cells.FontDirExc", "FontDirSet");

{{< /highlight >}}

{{% alert color="primary" %}}

Snälla notera följande:

- Ovanstående uttalande bör finnas i början av din ansökan.
- Att använda ovanstående tillvägagångssätt kräver inte att du ställer in teckensnittskatalogen med någon av FontConfigs-metoderna som diskuterats ovan.
- Strängen "FontDirSet" bör vara den fullständiga sökvägen till mappen som innehåller de nödvändiga typsnitten.

{{% /alert %}}
