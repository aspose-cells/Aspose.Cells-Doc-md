---
title: So geben Sie den Speicherort für TrueType-Schriftarten an
type: docs
weight: 30
url: /de/java/how-to-specify-truetype-fonts-location/
---
{{% alert color="primary" %}}

Dieser Artikel beschreibt:

1. [Wo die Aspose.Cells API nach TrueType-Schriftarten sucht](/cells/de/java/how-to-specify-truetype-fonts-location/#where-asposecells-looks-for-truetype-fonts-on-windows).
1. [So geben Sie explizit einen Ordner für TrueType-Schriftarten für Aspose.Cells API an](/cells/de/java/how-to-specify-truetype-fonts-location/#how-to-explicitly-specify-a-font-folder).
1. [So beschränken Sie die Aspose.Cells API auf die Verwendung von nur einem Speicherort für TrueType-Schriftarten](/cells/de/java/how-to-specify-truetype-fonts-location/#how-to-restrict-the-asposecells-to-use-only-one-font-folder).

{{% /alert %}}

## **Arbeiten mit Schriftarten**

### **Wobei Aspose.Cells auf Windows nach TrueType-Schriftarten sucht**

 Aspose.Cells sucht nach Schriften in der**Windows\Schriftarten** Mappe. Diese Standardeinstellung funktioniert die meiste Zeit, also geben Sie Ihre eigenen Schriftartenordner nur dann an, wenn Sie es wirklich brauchen.

### **Wobei Aspose.Cells unter Linux nach TrueType-Schriftarten sucht**

Standardmäßig sucht Aspose.Cells API an allen folgenden Orten nach den Schriftarten, obwohl verschiedene Linux-Distributionen Schriftarten in unterschiedlichen Ordnern speichern.

1. /usr/share/fonts
1. /usr/local/share/fonts

{{% alert color="primary" %}}

 Dieses Standardverhalten funktioniert für die meisten Linux-Distributionen, es ist jedoch nicht garantiert, dass es immer funktioniert. Möglicherweise müssen Sie den Speicherort der TrueType-Schriftarten explizit angeben.

{{% /alert %}}

### **So geben Sie einen Schriftordner explizit an**

Aspose.Cells APIs haben viele Factory-Methoden für die FontConfigs-Klasse verfügbar gemacht, um die Schriftarten oder Schriftartenordner wie unten beschrieben anzugeben.

1. Die setFontFolder-Methode akzeptiert den ersten Parameter vom Typ String mit der Position zum Fonts-Verzeichnis, während der zweite Parameter vom Typ Boolean die Aspose.Cells-APIs anweisen soll, die Ordner rekursiv nach Font-Dateien zu durchsuchen.
1. Die setFontFolders-Methode akzeptiert ein Array vom Typ String, sodass Sie mit diesem Ansatz viele Schriftartverzeichnisse angeben können. Sie können die Aspose.Cells-APIs auch anweisen, die Ordner rekursiv zu durchsuchen, indem Sie als zweiten Parameter „true“ angeben.
1. Die Methode setFontSources akzeptiert ein Array vom Typ FontSourceBase, damit Sie eine Liste mit den Speicherorten einzelner Schriftarten angeben können.

{{% alert color="primary" %}}

Wenn Sie den Schriftartenordner mit einer der oben genannten Methoden angeben, empfehlen wir, den Speicherort der Schriftart beim Start der Anwendung festzulegen, da Sie sonst möglicherweise schlecht formatierte Ergebnisse erhalten.

{{% /alert %}} {{% alert color="primary" %}}

Das Festlegen des Schriftartenordners mit einer der oben genannten Methoden stellt nicht sicher, dass der Aspose.Cells API nicht nach den Schriftarten an Standardspeicherorten wie dem Schriftartenordner des Systems sucht.

{{% /alert %}}

### **So beschränken Sie die Aspose.Cells auf die Verwendung nur eines Schriftartordners**

 Beginnend mit Aspose.Cells for Java 8.1.0, Festlegen der JVM-Argumente als**-DAspose.Cells.FontDirExc="IhrFontDir**stellt sicher, dass die Aspose.Cells API nur den angegebenen Schriftartenspeicherort verwendet.

Legen Sie die angegebenen Argumente mithilfe der System.setProperty-Methode wie unten gezeigt fest.

{{< highlight "java" >}}

System.setProperty("Aspose.Cells.FontDirExc", "FontDirSet");

{{< /highlight >}}

{{% alert color="primary" %}}

Bitte beachten Sie Folgendes:

- Die obige Erklärung sollte zu Beginn Ihrer Bewerbung stehen.
- Die Verwendung des obigen Ansatzes erfordert keine Einstellung des Schriftartenverzeichnisses mit einer der oben besprochenen FontConfigs-Methoden.
- Die Zeichenfolge "FontDirSet" sollte der vollständige Pfad zu dem Ordner sein, der die erforderlichen Schriftarten enthält.

{{% /alert %}}
