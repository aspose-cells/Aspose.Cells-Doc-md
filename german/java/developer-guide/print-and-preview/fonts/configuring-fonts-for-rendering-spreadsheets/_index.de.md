---
title: Konfigurieren von Schriftarten zur Darstellung von Tabellenkalkulationen
type: docs
weight: 10
url: /de/java/configuring-fonts-for-rendering-spreadsheets/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells APIs bieten die Möglichkeit, die Tabellenkalkulationen in Bildformate zu rendern und in PDF- und XPS-Formate zu konvertieren. Um die Konvertierungsgenauigkeit zu maximieren, ist es erforderlich, dass die in der Tabellenkalkulation verwendeten Schriftarten im Standard-Schriftartenverzeichnis des Betriebssystems verfügbar sind. Falls die erforderlichen Schriftarten nicht vorhanden sind, werden die Aspose.Cells APIs versuchen, die erforderlichen Schriftarten durch verfügbare zu ersetzen.

## **Auswahl von Schriftarten**

Im Folgenden wird der Prozess erläutert, den die Aspose.Cells-APIs im Hintergrund durchlaufen.

1. Die API versucht, die Schriftarten im Dateisystem zu finden, die dem exakten Schriftartnamen entsprechen, der in der Tabelle verwendet wird.
1. Wenn die API die Schriftarten mit genau demselben Namen nicht finden kann, versucht sie, die Standardschriftart unter dem [**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font)-Eigenschaft des Arbeitsblatts zu verwenden.
1. Wenn die API die unter [**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) definierte Schriftart nicht finden kann, versucht sie, die Schriftart unter [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) oder [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont) Eigenschaft zu verwenden.
1. Wenn die API die unter [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) oder [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont) definierte Schriftart nicht finden kann, versucht sie, die Schriftart unter [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName) Eigenschaft zu verwenden.
1. Wenn die API die unter [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName) definierte Schriftart nicht finden kann, versucht sie, die geeignetsten Schriftarten aus allen verfügbaren Schriftarten auszuwählen.
1. Schließlich rendert die API die Tabelle mit Arial, wenn sie keine Schriftarten im Dateisystem finden kann.

{{% alert color="primary" %}}

Die Aspose.Cells-APIs durchsuchen immer das Standard-Schriftartenverzeichnis des Betriebssystems, mit einer Ausnahme, und zwar wenn JVM-Argumente **-DAspose.Cells.FontDirExc="YourFontDir"** festgelegt sind. In diesem Fall überspringen die Aspose.Cells-APIs das Scannen des Standard-Schriftartenverzeichnisses des Betriebssystems und suchen nur den Pfad, wie in den oben genannten JVM-Argumenten angegeben.

{{% /alert %}}

## **Benutzerdefinierte Schriftartordner einstellen**

Aspose.Cells-APIs durchsuchen das Standard-Schriftartenverzeichnis des Betriebssystems nach den erforderlichen Schriftarten. Wenn die erforderlichen Schriftarten im Schriftartenordner des Systems nicht verfügbar sind, suchen die APIs in den benutzerdefinierten (benutzerdefinierten) Verzeichnissen. Die Klasse [**FontConfigs**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs) hat verschiedene Möglichkeiten freigelegt, benutzerdefinierte Schriftartenverzeichnisse wie unten aufgeführt festzulegen.

1. [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)): Diese Methode ist nützlich, wenn nur ein Ordner festgelegt werden soll.
1. [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean)): Diese Methode ist nützlich, wenn die Schriftarten in mehreren Ordnern vorhanden sind und der Benutzer alle Ordner separat einrichten möchte, anstatt alle Schriftarten in einem einzigen Ordner zu kombinieren.
1. [**FontConfigs.setFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontSources(com.aspose.cells.FontSourceBase[])): Diese Mechanismus ist nützlich, wenn der Benutzer Schriften aus mehreren Ordnern laden möchte oder eine einzelne Schriftdatei oder Schriftdaten aus einem Byte-Array.

{{% alert color="primary" %}}

Sowohl die Methoden [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)) als auch [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean)) akzeptieren als zweiten Parameter einen booleschen Typ. Durch Übergeben von **true** als zweiten Parameter werden die Aspose.Cells APIs angewiesen, in den Unterordnern nach den Schriftdateien zu suchen.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetCustomFontFolders-SetCustomFontFolders.java" >}}

{{% alert color="primary" %}}

Bitte verwenden Sie eine der oben genannten Methoden zu Beginn der Anwendung, d.h. bevor Sie andere Objekte der Aspose.Cells APIs aufrufen.

{{% /alert %}} {{% alert color="primary" %}}

Wenn mehr als eine der oben genannten Methoden zur Festlegung der Schriftartenquellen verwendet werden, tritt nur die letzte Einstellung in Kraft.

{{% /alert %}}

## **Schriftarten-Ersatzmechanismus**

Aspose.Cells APIs bieten auch die Möglichkeit, die Ersatzschrift für Rendering-Zwecke anzugeben. Dieser Mechanismus ist hilfreich, wenn eine erforderliche Schrift auf dem Rechner, auf dem die Konvertierung stattfinden soll, nicht verfügbar ist. Benutzer können eine Liste von Schriftarten als Alternative zur ursprünglich benötigten Schrift angeben. Um dies zu erreichen, haben die Aspose.Cells APIs die Methode FontConfigs.setFontSubstitutes freigegeben, die 2 Parameter akzeptiert. Der erste Parameter ist vom Typ **String** und sollte der Name der Schrift sein, die ersetzt werden muss. Der zweite Parameter ist ein Array vom Typ **String**. Benutzer können eine Liste von Schriftarten als Ersatz für die ursprüngliche Schrift (angegeben im ersten Parameter) angeben.

Hier ist ein einfaches Anwendungsbeispiel.

{{< highlight java >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[] { "Times New Roman", "Calibri" });

{{< /highlight >}}

## **Informationssammlung**

Neben den oben genannten Methoden bieten die Aspose.Cells APIs auch Möglichkeiten, Informationen darüber zu sammeln, welche Quellen und Substitutionen festgelegt wurden.

1. [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources--): Diese Methode gibt ein Array vom Typ [**FontSourceBase**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFontSource) zurück, das die Liste der angegebenen Schriftquellen enthält. Falls keine Quellen festgelegt wurden, gibt die Methode [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources--) ein leeres Array zurück.
1. [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String)): Diese Methode akzeptiert einen Parameter vom Typ **String**, um den Schriftname festzulegen, für den die Substitution vorgenommen wurde. Falls keine Substitution für den angegebenen Schriftnamen festgelegt wurde, gibt die Methode [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String)) null zurück.
