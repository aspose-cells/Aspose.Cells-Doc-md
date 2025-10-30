---
title: Lizenzierung
type: docs
weight: 50
url: /de/cpp/licensing/
---

## **Evaluierungsversion-Beschränkungen**
A free evaluation version of Aspose.Cells for C++ can be downloaded from the downloads section of Aspose's web site at: <https://downloads.aspose.com/cells/cpp>.
## **Lizenz mit Datei oder Stream-Objekt anwenden**
Die Lizenz kann aus einer Datei oder einem Stream-Objekt geladen werden. Aspose.Cells for C++ versucht die Lizenz an folgenden Orten zu finden:

1. Ausdrücklicher Pfad.
1. Der Ordner, der Aspose.Cells.dll enthält.
1. Der Ordner, der die Assembly enthält, die Aspose.Cells.dll aufgerufen hat.
1. Der Ordner, der die Einstiegsassembly (deine .exe) enthält.
1. Ein eingebettetes Ressource in der Assembly, die Aspose.Cells.dll aufgerufen hat.

Der einfachste Weg, eine Lizenz zu setzen, ist es, die Lizenzdatei in den gleichen Ordner wie die Aspose.Cells.dll-Datei zu legen und den Dateinamen ohne Pfad anzugeben, wie im folgenden Beispiel gezeigt.
### **Laden einer Lizenz aus Datei**
Der einfachste Weg, eine Lizenz anzuwenden, ist es, die Lizenzdatei in den gleichen Ordner wie die Aspose.Cells.dll-Datei zu legen und nur den Dateinamen ohne Pfad anzugeben.

{{% alert color="primary" %}} 

Wenn Sie die SetLicense-Methode aufrufen, sollte der Lizenzname, den Sie übergeben, dem Namen der Lizenzdatei entsprechen. Wenn Sie beispielsweise den Lizenzdateinamen in "Aspose.Cells.lic.xml" ändern, übergeben Sie diesen Dateinamen an die Cells->SetLicense(…)-Methode.

{{% /alert %}} 

**C++**

{{< highlight csharp >}}
  License license;
  license.SetLicense(u"Aspose.Cells.lic");

{{< /highlight >}}
### **Laden einer Lizenz aus einem Stream-Objekt**
Das folgende Beispiel zeigt, wie man eine Lizenz aus einem Stream lädt.

**C++**

{{< highlight csharp >}}

  License license;

  //You need to write your own code to read the contents of the license file into this variable.
  Vector<uint8_t> myStream{0}; //"Aspose.Cells.lic"

  license.SetLicense(myStream);

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
