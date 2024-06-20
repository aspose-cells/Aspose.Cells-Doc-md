---
title: Application d une licence
type: docs
weight: 40
url: /fr/java/applying-a-license/
---

{{% alert color="primary" %}}

Une fois que vous êtes satisfait de votre évaluation d'Aspose.Cells, [achetez une licence](https://purchase.aspose.com/buy) sur le site Web d'Aspose. Familiarisez-vous avec les différents [types de licence](https://purchase.aspose.com/policies/license-types/) offerts. Si vous avez des questions, n'hésitez pas à [contacter l'équipe commerciale d'Aspose](https://about.aspose.com/contact).

Chaque licence Aspose comprend un abonnement d'un an pour les mises à jour gratuites vers toutes les nouvelles versions ou correctifs qui sortent pendant cette période. Le support technique est gratuit et illimité et est fourni aussi bien aux utilisateurs titulaires d'une licence qu'aux utilisateurs en évaluation.

La licence est un fichier XML en texte brut qui contient des détails tels que le nom du produit, le nombre de développeurs autorisés, la date d'expiration de l'abonnement, etc. Le fichier est signé numériquement, donc ne le modifiez pas : même l'ajout d'un saut de ligne supplémentaire invalidera la licence.

Vous devez définir une licence avant d'effectuer des opérations avec des documents. Assurez-vous de le faire avant de créer un objet Document. Vous n'avez besoin de définir une licence qu'une seule fois par application ou processus.

{{% /alert %}}

## **Chargement du fichier de licence**

Dans Aspose.Cells pour Android via Java, la licence peut être [incorporée en tant que ressource](/cells/fr/java/applying-a-license/#applying-a-license-from-an-embedded-resource), ou chargée à partir d'un flux :

1. Placez le fichier de licence à n'importe quel emplacement sur **/mnt/sdcard/**.
1. Créez un flux qui fait référence au fichier.
1. Passez le flux (contenant le fichier de licence) à la méthode SetLicense.

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

### **Application d'une licence à partir d'une ressource incorporée**

Pour accéder à la licence en tant que ressource par nom à partir d'un fichier de package Android :

1. Ajoutez le fichier de licence en tant que ressource dans le dossier **res/raw** de votre application.
   Le fichier de licence devrait être visible dans le dossier **res/raw**.
1. Accédez/chargez la licence à partir de la ressource avec l'exemple de code suivant.

**Java**

{{< highlight java >}}

 License license = new License();

InputStream inputStream = getResources().openRawResource(R.raw.license);

license.setLicense(inputStream);

{{< /highlight >}}
