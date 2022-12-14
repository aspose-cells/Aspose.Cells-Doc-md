---
title: Ansöker om en licens
type: docs
weight: 40
url: /sv/java/applying-a-license/
---
{{% alert color="primary" %}}

 När du är nöjd med din utvärdering av Aspose.Cells,[köpa en licens](https://purchase.aspose.com/buy) på webbplatsen Aspose. Gör dig bekant med de olika[licenstyper](https://purchase.aspose.com/policies/license-types/) erbjuds. Om du har några frågor, tveka inte[kontakta Aspose säljteamet](https://about.aspose.com/contact).

Varje Aspose-licens innehåller en ettårsprenumeration för gratis uppgraderingar till alla nya versioner eller korrigeringar som kommer ut under denna tid. Teknisk support är gratis och obegränsad och tillhandahålls både till licensierade användare och utvärderingsanvändare.

Licensen är en XML-fil i vanlig text som innehåller detaljer som produktnamn, antal licensierade utvecklare, prenumerations utgångsdatum och så vidare. Filen är digitalt signerad, så ändra inte filen: även om du lägger till en extra radbrytning i filen blir den ogiltig.

Du måste ange en licens innan du utför några operationer med dokument. Se till att du gör detta innan du skapar ett dokumentobjekt. Du behöver bara ange en licens en gång per ansökan eller process.

{{% /alert %}}

## **Laddar licensfilen**

 I Aspose.Cells för Android via Java kan licensen vara[inbäddad som en resurs](/cells/sv/java/applying-a-license/#applying-a-license-from-an-embedded-resource), eller laddas från en stream:

1.  Placera licensfilen var som helst på**/mnt/sdcard/**.
1. Skapa en ström som refererar till fil.
1. Skicka strömmen (som innehåller licensfilen) till SetLicense-metoden.

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

### **Tillämpa en licens från en inbäddad resurs**

Så här kommer du åt licensen som en resurs efter namn från en Android-paketfil:

1.  Lägg till licensfilen som en resurs till din applikation**res/rå** mapp.
 Licensfilen ska vara synlig i**res/rå** mapp.
1. Få åtkomst till/ladda in licensen från resursen med följande kodexempel.

**Java**

{{< highlight "java" >}}

 License license = new License();

InputStream inputStream = getResources().openRawResource(R.raw.license);

license.setLicense(inputStream);

{{< /highlight >}}
