---
title: Seiteneinrichtung und Druckoptionen
type: docs
weight: 10
url: /de/java/page-setup-and-printing-options/
---

{{% alert color="primary" %}}

Manchmal müssen Entwickler die Seiteneinrichtung und die Druckeinstellungen konfigurieren, um den Druckprozess zu steuern. Die Seiteneinrichtung und Druckeinstellungen bieten verschiedene Optionen und werden von Aspose.Cells vollständig unterstützt.

Dieser Artikel zeigt, wie Sie mithilfe der Aspose.Cells-API eine Konsolenanwendung erstellen und Seitenlayout- und Druckoptionen auf einem Arbeitsblatt mit wenigen einfachen Codezeilen anwenden.

{{% /alert %}}

## **Arbeiten mit Seiten- und Druckeinstellungen**

Für dieses Beispiel haben wir eine Arbeitsmappe in Microsoft Excel erstellt und Aspose.Cells verwendet, um die Seiteneinrichtung und Druckoptionen festzulegen.

### **Einstellen von Seitenlayoutoptionen**

Erstellen Sie zuerst ein einfaches Arbeitsblatt in Microsoft Excel. Wenden Sie dann Seiteneinrichtungsoptionen darauf an. Das Ausführen des Codes ändert die Seiteneinrichtungsoptionen, wie im Screenshot unten dargestellt.

**Ausgabedatei** 

![todo:image_alt_text](page-setup-and-printing-options_1.png)

1. Erstellen Sie ein Arbeitsblatt mit einigen Daten in Microsoft Excel:
   1. Öffnen Sie eine neue Arbeitsmappe in Microsoft Excel.
   1. Fügen Sie einige Daten hinzu.
      Im Folgenden ist ein Screenshot der Datei zu sehen.

      **Eingabedatei**

![todo:image_alt_text](page-setup-and-printing-options_2.png)

1. Legen Sie Seiteneinrichtungsoptionen fest:
   Wenden Sie die Seiteneinrichtungsoptionen auf die Datei an. Unten ist ein Screenshot der Standardoptionen vor der Anwendung der neuen Optionen zu sehen.

   **Standardseitenlayoutoptionen**

![todo:image_alt_text](page-setup-and-printing-options_3.png)

1. Laden Sie Aspose.Cells herunter und installieren Sie es:
   1. [Herunterladen](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
   1. Entpacken Sie es auf Ihrem Entwicklungscomputer.
      Alle [Aspose](http://www.aspose.com/) Komponenten funktionieren nach der Installation im Evaluierungsmodus. Der Evaluierungsmodus hat kein Zeitlimit und fügt nur Wasserzeichen in erstellte Dokumente ein.
1. Ein Projekt erstellen.
   Erstellen Sie entweder ein Projekt mithilfe eines Java-Editors, z. B. Eclipse, oder erstellen Sie ein einfaches Programm mithilfe eines Texteditors.
1. Einen Klassenpfad hinzufügen.
   1. Extrahieren Sie die Aspose.Cells.jar und dom4j_1.6.1.jar aus Aspose.Cells.zip.
   1. Setzen Sie den Klassenpfad des Projekts in Eclipse:
   Wählen Sie in Eclipse Ihr Projekt aus, und klicken Sie dann auf **Projekt** gefolgt von **Eigenschaften**.
   Wählen Sie links in der Dialogfeld **Java Build Path** aus.
   Wählen Sie den Registerkarte Bibliotheken, klicken Sie auf **JARs hinzufügen** oder **Externe JARs hinzufügen**, um Aspose.Cells.jar und dom4j_1.6.1.jar auszuwählen und sie den Build-Pfaden hinzuzufügen.
      Oder Sie können es zur Laufzeit an einer Eingabeaufforderung in Windows festlegen:

{{< highlight java >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

1. Schreiben Sie die Anwendung, die APIs aufruft:
   Im Folgenden finden Sie den Code, der von der Komponente in diesem Beispiel verwendet wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPageSetupOptions-SettingPageSetupOptions.java" >}}

### **Druckoptionen festlegen**

Die Seiteneinrichtungseinstellungen bieten auch mehrere Druckoptionen (auch Blattoptionen genannt), mit denen Benutzer steuern können, wie Arbeitsblattseiten gedruckt werden. Sie ermöglichen Benutzern:

- Eine bestimmte Druckbereich eines Arbeitsblatts auswählen.
- Titel drucken.
- Gitternetzlinien drucken.
- Zeilen-/Spaltenüberschriften drucken.
- Entwurfsqualität erreichen.
- Kommentare drucken.
- Zellenfehler drucken.
- Seiteneinteilung definieren.

Das folgende Beispiel wendet Druckoptionen auf die Datei an, die im obigen Beispiel erstellt wurde (PageSetup.xls). Der nachfolgende Screenshot zeigt die Standard-Druckoptionen, bevor neue Optionen angewendet werden.
**Eingabedokument**

![todo:image_alt_text](page-setup-and-printing-options_4.png)

Das Ausführen des Codes ändert die Druckoptionen.
**Ausgabedatei**

![todo:image_alt_text](page-setup-and-printing-options_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPrintoptions-SettingPrintoptions.java" >}}

## **Zusammenfassung**

{{% alert color="primary" %}}

Dieser Artikel zeigt, wie die Seiten- und Blattdruckoptionen mit Aspose.Cells festgelegt werden können. Hoffentlich gibt er Ihnen einige Einblicke, und Sie können diese Optionen in Ihren eigenen Szenarien verwenden.

Aspose.Cells profitiert von jahrelanger Forschung, Design und sorgfältiger Abstimmung. Wir begrüßen herzlich Ihre Anfragen, Kommentare und Vorschläge im [Aspose.Cells Forum](https://forum.aspose.com/c/cells/9). Wir garantieren eine schnelle Antwort.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
