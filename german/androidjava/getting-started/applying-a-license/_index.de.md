---
title: Anwenden einer Lizenz
type: docs
weight: 40
url: /de/java/applying-a-license/
---
{{% alert color="primary" %}}

 Sobald Sie mit Ihrer Bewertung von Aspose.Cells zufrieden sind,[eine Lizenz kaufen](https://purchase.aspose.com/buy) auf der Website Aspose. Machen Sie sich mit den Unterschieden vertraut[Lizenztypen](https://purchase.aspose.com/policies/license-types/) angeboten. Wenn Sie Fragen haben, zögern Sie nicht[Wenden Sie sich an das Verkaufsteam unter Aspose](https://about.aspose.com/contact).

Jede Aspose-Lizenz enthält ein einjähriges Abonnement für kostenlose Upgrades auf alle neuen Versionen oder Fixes, die während dieser Zeit herauskommen. Der technische Support ist kostenlos und unbegrenzt und wird sowohl lizenzierten als auch Testbenutzern zur Verfügung gestellt.

Die Lizenz ist eine reine Text-XML-Datei, die Details wie den Produktnamen, die Anzahl der lizenzierten Entwickler, das Ablaufdatum des Abonnements usw. enthält. Die Datei ist digital signiert, ändern Sie die Datei also nicht: Selbst das Hinzufügen eines zusätzlichen Zeilenumbruchs in der Datei macht sie ungültig.

Sie müssen eine Lizenz festlegen, bevor Sie Vorgänge mit Dokumenten durchführen. Stellen Sie sicher, dass Sie dies tun, bevor Sie ein Document-Objekt erstellen. Sie müssen nur einmal pro Anwendung oder Prozess eine Lizenz festlegen.

{{% /alert %}}

## **Laden der Lizenzdatei**

 In Aspose.Cells für Android über Java kann die Lizenz sein[als Ressource eingebettet](/cells/de/java/applying-a-license/#applying-a-license-from-an-embedded-resource), oder aus einem Stream geladen:

1.  Legen Sie die Lizenzdatei an einer beliebigen Stelle ab**/mnt/sdcard/**.
1. Erstellen Sie einen Stream, der auf eine Datei verweist.
1. Übergeben Sie den Stream (der die Lizenzdatei enthält) an die SetLicense-Methode.

**Java**

{{< highlight "java" >}}

 String dataDir = Environment.getExternalStorageDirectory().getPath() + "/";

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream(dataDir + "Aspose.Cells.Android.lic");

// Instantiate the License class

License license = new License();

//Set the license through the stream object

license.setLicense(fstream);

{{< /highlight >}}

### **Anwenden einer Lizenz von einer eingebetteten Ressource**

So greifen Sie über den Namen einer Android-Paketdatei auf die Lizenz als Ressource zu:

1.  Fügen Sie die Lizenzdatei Ihrer Anwendung als Ressource hinzu**res/roh** Mappe.
 Die Lizenzdatei sollte in der sichtbar sein**res/roh** Mappe.
1. Greifen Sie mit dem folgenden Codebeispiel auf die Lizenz zu bzw. laden Sie sie von der Ressource.

**Java**

{{< highlight "java" >}}

 License license = new License();

InputStream inputStream = getResources().openRawResource(R.raw.license);

license.setLicense(inputStream);

{{< /highlight >}}
