---
title: Lizenz anwenden
type: docs
weight: 40
url: /de/java/applying-a-license/
---

{{% alert color="primary" %}}

Sobald Sie mit Ihrer Auswertung von Aspose.Cells zufrieden sind, [kaufen Sie eine Lizenz](https://purchase.aspose.com/buy) auf der Aspose-Website. Machen Sie sich mit den verschiedenen [Lizenztypen](https://purchase.aspose.com/policies/license-types/) vertraut, die angeboten werden. Wenn Sie Fragen haben, zögern Sie nicht, [das Vertriebsteam von Aspose zu kontaktieren](https://about.aspose.com/contact).

Jede Aspose-Lizenz beinhaltet ein einjähriges Abonnement für kostenlose Upgrades auf alle neuen Versionen oder Fixes, die während dieser Zeit veröffentlicht werden. Der technische Support ist kostenlos und unbegrenzt und wird sowohl für lizenzierte als auch für Evaluierungsnutzer bereitgestellt.

Die Lizenz ist eine einfache Text-XML-Datei, die Details wie den Produktnamen, die Anzahl der lizenzierten Entwickler, das Ablaufdatum des Abonnements usw. enthält. Datei ist digital signiert, daher dürfen Sie die Datei nicht ändern: Selbst das Hinzufügen eines zusätzlichen Zeilenumbruchs in die Datei macht sie ungültig.

Sie müssen eine Lizenz festlegen, bevor Sie irgendwelche Operationen mit Dokumenten durchführen. Stellen Sie sicher, dass Sie dies vor dem Erstellen eines Document-Objekts tun. Sie müssen die Lizenz nur einmal pro Anwendung oder Prozess festlegen.

{{% /alert %}}

## **Laden der Lizenzdatei**

In Aspose.Cells für Android via Java kann die Lizenz [als Ressource eingebettet](/cells/de/java/applying-a-license/#applying-a-license-from-an-embedded-resource) oder aus einem Stream geladen werden:

1. Legen Sie die Lizenzdatei an einem beliebigen Ort auf **/mnt/sdcard/** ab.
1. Erstellen Sie einen Stream, der auf die Datei verweist.
1. Geben Sie den Stream (mit der Lizenzdatei) in die SetLicense-Methode ein.

**Java**

{{< highlight java >}}

 String dataDir = Environment.getExternalStorageDirectory().getPath() + "/";

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream(dataDir + "Aspose.Cells.Android.lic");

// Instantiate the License class

License license = new License();

//Set the license through the stream object

license.setLicense(fstream);

{{< /highlight >}}

### **Anwendung einer Lizenz aus einer eingebetteten Ressource**

Um auf die Lizenz als Ressource nach Namen aus einer Android-Paketdatei zuzugreifen:

1. Fügen Sie die Lizenzdatei als Ressource zu dem Ordner **res/raw** Ihrer Anwendung hinzu.
   Die Lizenzdatei sollte im Ordner **res/raw** sichtbar sein.
1. Greifen Sie/laden Sie die Lizenz aus der Ressource mit dem folgenden Codebeispiel.

**Java**

{{< highlight java >}}

 License license = new License();

InputStream inputStream = getResources().openRawResource(R.raw.license);

license.setLicense(inputStream);

{{< /highlight >}}
