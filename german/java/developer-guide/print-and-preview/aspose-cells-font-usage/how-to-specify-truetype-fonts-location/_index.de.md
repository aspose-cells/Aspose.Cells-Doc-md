---
title: So geben Sie den Speicherort von TrueType Schriftarten an
type: docs
weight: 30
url: /de/java/how-to-specify-truetype-fonts-location/
---

{{% alert color="primary" %}}

Dieser Artikel beschreibt:

1. [Wo die Aspose.Cells API nach TrueType-Schriftarten sucht](/cells/de/java/how-to-specify-truetype-fonts-location/#where-asposecells-looks-for-truetype-fonts-on-windows).
1. [Wie man explizit einen Ordner für TrueType-Schriftarten für die Aspose.Cells API festlegt](/cells/de/java/how-to-specify-truetype-fonts-location/#how-to-explicitly-specify-a-font-folder).
1. [Wie man die Aspose.Cells API einschränkt, nur einen Speicherort für TrueType-Schriften zu verwenden](/cells/de/java/how-to-specify-truetype-fonts-location/#how-to-restrict-the-asposecells-to-use-only-one-font-folder).

{{% /alert %}}

## **Arbeiten mit Schriftarten**

### **Wo Aspose.Cells nach TrueType-Schriftarten auf Windows sucht**

Aspose.Cells sucht nach Schriftarten im **Windows\Fonts**-Ordner. Diese Standardeinstellung funktioniert in den meisten Fällen, geben Sie also nur Ihre eigenen Schriftordner an, wenn es wirklich nötig ist.

### **Wo Aspose.Cells nach TrueType-Schriftarten auf Linux sucht**

Standardmäßig sucht die Aspose.Cells-API in allen folgenden Orten nach Schriftarten, obwohl verschiedene Linux-Distributionen Schriftarten in verschiedenen Ordnern speichern.

1. /usr/share/fonts
1. /usr/local/share/fonts

{{% alert color="primary" %}}

Dieses Standardverhalten funktioniert für die meisten Linux-Distributionen, ist jedoch nicht garantiert, dass es immer funktioniert. Sie müssen möglicherweise den Speicherort der TrueType-Schriftarten explizit angeben. 

{{% /alert %}}

### **Wie man einen Schriftartenordner explizit angibt**

Die APIs von Aspose.Cells haben viele Factory-Methoden für die Klasse FontConfigs freigelegt, um die Schriftarten oder Schriftartenordner wie unten beschrieben anzugeben.

1. Die Methode setFontFolder akzeptiert als ersten Parameter einen String vom Typ String mit dem Speicherort des Schriftartenverzeichnisses, während der zweite Parameter vom Typ Boolean dazu dient, die Aspose.Cells-APIs anzuweisen, die Ordner rekursiv nach Schriftdateien zu durchsuchen.
1. Die Methode setFontFolders akzeptiert ein Array vom Typ String, sodass Sie viele Schriftverzeichnisse auf diese Weise angeben können. Sie können auch die Aspose.Cells-APIs anweisen, die Ordner rekursiv zu durchsuchen, indem Sie true als zweiten Parameter festlegen.
1. Die Methode setFontSources akzeptiert ein Array vom Typ FontSourceBase, um eine Liste der einzelnen Schriftartenstandorte anzugeben.

{{% alert color="primary" %}}

Beim Angeben des Schriftartenordners mit einer der oben genannten Methoden empfehlen wir, den Schriftartenstandort zu Beginn der Anwendung festzulegen, da Sie ansonsten schlecht formatierte Ergebnisse erhalten können.

{{% /alert %}} {{% alert color="primary" %}}

Das Festlegen des Schriftartenordners mit einer der oben genannten Methoden garantiert nicht, dass die Aspose.Cells-API nicht nach den Schriftarten in Standardpositionen wie dem Schriftartenordner des Systems sucht.

{{% /alert %}}

### **Wie man Aspose.Cells einschränkt, nur einen Schriftartenordner zu verwenden**

Ab Aspose.Cells for Java 8.1.0 stellt das Festlegen der JVM-Argumente als **-DAspose.Cells.FontDirExc="YourFontDir** sicher, dass die Aspose.Cells-API nur die Schriftartenposition wie angegeben verwendet.

Legen Sie die angegebenen Argumente wie unten gezeigt mit der System.setProperty-Methode fest.

{{< highlight java >}}

System.setProperty("Aspose.Cells.FontDirExc", "FontDirSet");

{{< /highlight >}}

{{% alert color="primary" %}}

Bitte beachten Sie Folgendes:

- Die obige Aussage sollte zu Beginn Ihrer Anwendung stehen.
- Bei diesem Ansatz ist es nicht erforderlich, das Schriftartenverzeichnis mit einer der oben diskutierten Methoden von FontConfigs festzulegen.
- Der String "FontDirSet" sollte der vollständige Pfad zum Ordner sein, der die erforderlichen Schriftarten enthält.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
