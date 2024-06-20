---
title: Tillämpa en licens
type: docs
weight: 40
url: /sv/java/applying-a-license/
---

{{% alert color="primary" %}}

När du är nöjd med din utvärdering av Aspose.Cells, [köp en licens](https://purchase.aspose.com/buy) på Aspose-webbplatsen. Bli bekant med de olika [licenstyperna](https://purchase.aspose.com/policies/license-types/) som erbjuds. Om du har några frågor, tveka inte att [kontakta Aspose-försäljningsteamet](https://about.aspose.com/contact).

Varje Aspose-licens har ett års prenumeration för gratis uppgraderingar till alla nya versioner eller fixar som kommer ut under denna tid. Teknisk support är gratis och obegränsad och tillhandahålls både till licensierade och utvärderingsanvändare.

Licensen är en ren text XML-fil som innehåller detaljer som produktnamn, antal licensierade utvecklare, prenumerations utgångsdatum osv. Filen är digitalt signerad, så ändra inte filen: även att lägga till en extra radbrytning i filen kommer ogiltigförklara den.

Du måste ställa in en licens innan du utför några åtgärder med dokument. Se till att du gör detta innan du skapar ett dokumentobjekt. Du behöver bara ställa in en licens en gång per applikation eller process.

{{% /alert %}}

## **Ladda Licensfilen**

I Aspose.Cells för Android via Java kan licensen [bäddas in som en resurs](/cells/sv/java/applying-a-license/#applying-a-license-from-an-embedded-resource), eller laddas från en ström:

1. Placera licensfilen på valfri plats på **/mnt/sdcard/**.
1. Skapa en ström som refererar filen.
1. Skicka strömmen (som innehåller licensfilen) till SetLicense-metoden.

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

### **Tillämpa en licens från en inbäddad resurs**

För att få åtkomst till licensen som en resurs efter namn från en Android-paketfil:

1. Lägg till licensfilen som en resurs i din applikations **res/raw** -mapp.
   Licensfilen ska vara synlig i **res/raw** -mappen.
1. Få åtkomst/ladda licensen från resursen med följande kodprov.

**Java**

{{< highlight java >}}

 License license = new License();

InputStream inputStream = getResources().openRawResource(R.raw.license);

license.setLicense(inputStream);

{{< /highlight >}}
