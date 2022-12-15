---
title: Appliquer une licence
type: docs
weight: 40
url: /fr/java/applying-a-license/
---
{{% alert color="primary" %}}

 Une fois que vous êtes satisfait de votre évaluation du Aspose.Cells,[acheter une licence](https://purchase.aspose.com/buy) sur le site Aspose. Familiarisez-vous avec les différents[types de licence](https://purchase.aspose.com/policies/license-types/) offert. Si vous avez des questions, n'hésitez pas à[contacter l'équipe commerciale Aspose](https://about.aspose.com/contact).

Chaque licence Aspose comporte un abonnement d'un an pour des mises à niveau gratuites vers toutes les nouvelles versions ou correctifs qui sortent pendant cette période. Le support technique est gratuit et illimité et fourni à la fois aux utilisateurs sous licence et aux utilisateurs d'évaluation.

La licence est un fichier XML en texte brut qui contient des détails tels que le nom du produit, le nombre de développeurs sous licence, la date d'expiration de l'abonnement, etc. Le fichier est signé numériquement, ne modifiez donc pas le fichier : même l'ajout d'un saut de ligne supplémentaire dans le fichier l'invalidera.

Vous devez définir une licence avant d'effectuer toute opération avec des documents. Assurez-vous de le faire avant de créer un objet Document. Vous n'êtes tenu de définir une licence qu'une seule fois par application ou processus.

{{% /alert %}}

## **Chargement du fichier de licence**

 Dans Aspose.Cells for Android via Java, la licence peut être[intégré en tant que ressource](/cells/fr/java/applying-a-license/#applying-a-license-from-an-embedded-resource), ou chargé à partir d'un flux :

1.  Placez le fichier de licence à n'importe quel endroit sur**/mnt/sdcard/**.
1. Créez un flux qui référence le fichier.
1. Transmettez le flux (contenant le fichier de licence) à la méthode SetLicense.

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

### **Application d'une licence à partir d'une ressource intégrée**

Pour accéder à la licence en tant que ressource par nom à partir d'un fichier de package Android :

1.  Ajoutez le fichier de licence en tant que ressource à votre application**res/brut** dossier.
 Le fichier de licence doit être visible dans le**res/brut** dossier.
1. Accédez/chargez la licence à partir de la ressource avec l'exemple de code suivant.

**Java**

{{< highlight "java" >}}

 License license = new License();

InputStream inputStream = getResources().openRawResource(R.raw.license);

license.setLicense(inputStream);

{{< /highlight >}}
