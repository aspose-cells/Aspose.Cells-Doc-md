---
title: No overload for method Save takes 4 arguments [Keine Überladung für die Methode Speichern nimmt 4 Argumente]
type: docs
weight: 70
url: /de/net/no-overload-for-method-save-takes-4-arguments/
---

## **Symptom**

"Bei Verwendung von Aspose.Cells version erhalte ich diesen Fehler, wenn ich die Save-Methode beim Versuch, Arbeitsmappe in das Antwortobjekt zu speichern. Ich finde diesen Codeschnipsel in der Online-Dokumentation."

### **Screenshot des Fehlers**

![todo:image_alt_text](no-overload-for-method-save-takes-4-arguments_1.png)

### **Lösung**

Please use **.NET 2.0** compiled version of the product as it works fine on VS.NET 2008/2010. Actually we provide separate dll's for different environments, project types and systems etc. For reference, please check:<https://docs.aspose.com/cells/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/>

Aspose.Cells for .NET ist kompatibel und funktioniert einwandfrei mit allen .NET-Framework-Versionen wie 2.x, 3.x, 4.x usw. für jeden Projekttyp, z.B. Asp.NET/Winforms, Webprojekt, Windows/Web Service, Konsolenanwendung oder andere Projekte usw. Wir stellen verschiedene dlls für verschiedene .NET-Framework-Versionen bereit. Für weitere Informationen lesen Sie die **readme.txt**-Datei im "\Bin"-Ordner unter Ihrem Installationsverzeichnis. Aber diese **readme.txt**-Datei ist vorhanden.

Wenn Sie unser Produkt in einer Webanwendung verwenden, verwenden Sie bitte die Aspose.Cells.dll aus dem Ordner **NET 2.0** im "/bin"-Verzeichnis. Zur Information, die dll im **.NET 3.5-Clientprofil**-Verzeichnis wird nur für die Konsolenanwendung mit dem Net Frame Clientprofil als Zielframework von VS.NET verwendet. Überprüfen Sie Ihr Projekt, möglicherweise verweist Ihr Projekt auf diese dll.

### **Verweise**

<https://forum.aspose.com/t/overload-for-method-save-of-workbook-takes-4-arguments-involving-response-object/121465/1>
