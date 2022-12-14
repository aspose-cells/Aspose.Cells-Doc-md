---
title: Lizenzierung
type: docs
weight: 50
url: /de/cpp/licensing/
---
## **Einschränkungen der Evaluierungsversion**
 Eine kostenlose Evaluierungsversion von Aspose.Cells für C++ kann im Download-Bereich der Website von Aspose heruntergeladen werden unter:<https://downloads.aspose.com/cells/cpp>.
## **Wenden Sie die Lizenz mit dem Datei- oder Stream-Objekt an**
Die Lizenz kann aus einer Datei oder einem Stream-Objekt geladen werden. Aspose.Cells für C++ wird versuchen, die Lizenz an den folgenden Orten zu finden:

1. Explizite Pfad.
1. Der Ordner, der Aspose.Cells.dll enthält.
1. Der Ordner, der die Assembly mit dem Namen Aspose.Cells.dll enthält.
1. Der Ordner, der die Eintragsassembly enthält (Ihre .exe).
1. Eine eingebettete Ressource in der Assembly, die Aspose.Cells.dll aufgerufen hat.

Der einfachste Weg, eine Lizenz festzulegen, besteht darin, die Lizenzdatei in denselben Ordner wie die Datei Aspose.Cells.dll zu legen und den Dateinamen ohne Pfad anzugeben, wie im folgenden Beispiel gezeigt.
### **Laden einer Lizenz aus einer Datei**
Der einfachste Weg, eine Lizenz anzuwenden, besteht darin, die Lizenzdatei in denselben Ordner wie die Datei Aspose.Cells.dll zu legen und nur den Dateinamen ohne Pfad anzugeben.

{{% alert color="primary" %}} 

Wenn Sie die SetLicense-Methode aufrufen, sollte der Lizenzname, den Sie übergeben, der der Lizenzdatei sein. Wenn Sie beispielsweise den Namen der Lizenzdatei in „Aspose.Cells.lic.xml“ ändern, übergeben Sie diesen Dateinamen an die Methode Cells->SetLicense(…).

{{% /alert %}} 

**C++**

{{< highlight "csharp" >}}

 intrusive_ptr<License> license = new License();

license->SetLicense(new String("Aspose.Cells.lic"));

{{< /highlight >}}
### **Laden einer Lizenz aus einem Stream-Objekt**
Das folgende Beispiel zeigt, wie eine Lizenz aus einem Stream geladen wird.

**C++**

{{< highlight "csharp" >}}

 intrusive_ptr<License>license = new License();

intrusive_ptr<FileStream> myStream = new FileStream(new String("Aspose.Cells.lic"), FileMode_Open);

license->SetLicense(myStream);

{{< /highlight >}}
