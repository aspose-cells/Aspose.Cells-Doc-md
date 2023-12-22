---
title: Licensing
type: docs
weight: 50
url: /de/cpp/licensing/
---
##  **Einschränkungen der Evaluierungsversion**
 Eine kostenlose Testversion von Aspose.Cells for C++ kann im Download-Bereich der Website von Aspose heruntergeladen werden:<https://downloads.aspose.com/cells/cpp>.
##  **Wenden Sie die Lizenz mithilfe einer Datei oder eines Stream-Objekts an**
Die Lizenz kann aus einer Datei oder einem Stream-Objekt geladen werden. Aspose.Cells for C++ wird versuchen, die Lizenz an den folgenden Orten zu finden:

1. Expliziter Pfad.
1. Der Ordner, der Aspose.Cells.dll enthält.
1. Der Ordner, der die Assembly enthält, die Aspose.Cells.dll aufgerufen hat.
1. Der Ordner, der die Eintragsassembly (Ihre EXE-Datei) enthält.
1. Eine eingebettete Ressource in der Assembly mit dem Namen Aspose.Cells.dll.

Der einfachste Weg, eine Lizenz festzulegen, besteht darin, die Lizenzdatei im selben Ordner wie die Datei Aspose.Cells.dll abzulegen und den Dateinamen ohne Pfad anzugeben, wie im folgenden Beispiel gezeigt.
###  **Laden einer Lizenz aus einer Datei**
Der einfachste Weg, eine Lizenz anzuwenden, besteht darin, die Lizenzdatei im selben Ordner wie die Datei Aspose.Cells.dll abzulegen und nur den Dateinamen ohne Pfad anzugeben.

{{% alert color="primary" %}} 

Wenn Sie die SetLicense-Methode aufrufen, sollte der von Ihnen übergebene Lizenzname der der Lizenzdatei sein. Wenn Sie beispielsweise den Namen der Lizenzdatei in „Aspose.Cells.lic.xml“ ändern, übergeben Sie diesen Dateinamen an die Methode Cells->SetLicense(…).

{{% /alert %}} 

**C++**

{{< highlight "csharp" >}}
  License license;
  license.SetLicense(u"Aspose.Cells.lic");

{{< /highlight >}}
###  **Laden einer Lizenz aus einem Stream-Objekt**
Das folgende Beispiel zeigt, wie eine Lizenz aus einem Stream geladen wird.

**C++**

{{< highlight "csharp" >}}

  License license;

  //You need to write your own code to read the contents of the license file into this variable.
  Vector<uint8_t> myStream{0}; //"Aspose.Cells.lic"

  license.SetLicense(myStream);

{{< /highlight >}}
