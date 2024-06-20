---
title: Installation d Aspose.Cells pour Android via Java
type: docs
weight: 30
url: /fr/java/aspose-cells-for-android-via-java-installation/
---

## **Configuration requise**
Aspose.Cells pour Android via Java est indépendant de la plateforme et peut être utilisé sur n'importe quelle plateforme où l'environnement d'exécution Android est installé et fonctionnera sur des systèmes Android exécutant Android OS 2.0 ou ultérieur. À l'heure actuelle, le composant a été testé avec :

- Android 5.1 v 22
## **Installer Aspose.Cells pour Android via Java à partir du dépôt Maven**
1. Ajoutez le dépôt Maven dans votre build.gradle 
1. Ajoutez le JAR 'Aspose.Cells pour Android via Java' en tant que dépendance

{{< highlight java >}}

 // 1. Add maven repository into your build.gradle 

repositories {

    mavenCentral()

    maven { url "http://repository.aspose.com/repo/" }

}

// 2. Add 'Aspose.Cells for Android via Java' JAR as a dependency

dependencies {

    ...

    ...

    compile (group: 'com.aspose', name: 'aspose-cells', version: '20.6', classifier: 'android.via.java')

}

{{< /highlight >}}
## **Comment utiliser Aspose.Cells pour Android via Java**
Ce sujet vous guidera à travers les étapes nécessaires pour configurer Aspose.Cells pour Android via Java dans l'IDE Android Studio, en supposant que vous avez déjà la dernière version d'Android Studio installée sur votre machine et que vous avez également acquis la dernière version du package Aspose.Cells pour Android via Java.

{{% alert color="primary" %}} 

Si vous n'avez pas encore installé Android Studio, vous devez d'abord acquérir la configuration d'Android Studio et l'installer sur votre machine. Vous pouvez télécharger la dernière version d'Android Studio depuis [ici](https://developer.android.com/studio/index.html#win-bundle) alors que les détails sur la manière d'installer l'IDE sont disponibles [ici](https://developer.android.com/studio/install.html).

{{% /alert %}} {{% alert color="primary" %}} 

Le package Aspose.Cells pour Android via Java peut être téléchargé à partir de [ici](https://downloads.aspose.com/cells/androidjava). Veuillez noter que chaque package de publication d'Aspose.Cells pour Android via Java se compose principalement de 2 fichiers comme détaillé ci-dessous.

- **aspose-cells-x.x.x.jar** est le fichier de bibliothèque principal contenant tous les espaces de noms de l'API Aspose.Cells pour Android via Java.
- **aspose-cells-x.x.x-libs.apk** est l'APK contenant le fichier bcprov-jdk15-146.jar de tierce partie utilisé pour les fonctions de chiffrement et de déchiffrement offertes par l'API Aspose.Cells pour Android via Java.

{{% /alert %}} 
### **Démarrer avec Aspose.Cells pour Android via Java dans Android Studio**
Une fois que l'IDE Android Studio est chargé, cliquez sur Fichier > Nouveau > Nouveau Projet comme indiqué ci-dessous.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_1.png)

Vous pouvez également créer un nouveau projet à partir de l'écran d'accueil d'Android Studio comme indiqué ci-dessous.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_2.png)

Ensuite, vous serez invité à spécifier le nom de l'application, le domaine et l'emplacement pour stocker les fichiers du projet. Vous pouvez choisir de modifier les valeurs par défaut selon votre choix ou les laisser telles quelles, et cliquer sur Suivant.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_3.png)

À l'étape suivante, vous devez spécifier le périphérique Android sur lequel vous souhaitez héberger/exécuter votre application. Une fois sélectionné, cliquez sur le bouton Suivant.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_4.png)

Maintenant, vous devez sélectionner l'activité dans une liste prédéfinie de modèles. Pour garder la démonstration simple, nous avons sélectionné le modèle d'activité vide comme indiqué ci-dessous.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_5.png)

Cliquez sur le bouton Terminer sur la boîte de dialogue Personnaliser l'activité car nous allons conserver tous les paramètres par défaut tels qu'ils sont.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_6.png)

Dès que vous cliquez sur le bouton Terminer à l'étape précédente, l'IDE commencera à construire le projet comme indiqué ci-dessous. Laissez-le finir ou cliquez sur le bouton Annuler.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_7.png)

Maintenant que le projet a été chargé dans l'IDE, vous pouvez souhaiter changer la vue en Vue Project pour voir la hiérarchie complète des fichiers du projet. Pour changer la vue, veuillez consulter la capture d'écran suivante.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_8.png)

Après avoir changé la vue en Projet, recherchez et chargez le fichier **build.gradle** dans l'éditeur et collez le fragment suivant comme indiqué ci-dessous.

{{< highlight java >}}

 dexOptions{

    javaMaxHeapSize "4g"

}

{{< /highlight >}}

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_9.png)

Ensuite, nous allons ajouter le Jar Aspose.Cells pour Android via Java au projet. Il y a 2 étapes importantes détaillées ci-dessous.

- Copiez manuellement le Jar Aspose.Cells pour Android via Java dans le dossier **\app\libs**.
- Ajoutez le Jar Aspose.Cells pour Android via Java comme bibliothèque au module comme indiqué ci-dessous.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_10.png)

Vous serez invité à sélectionner le module auquel vous souhaitez ajouter le Jar Aspose.Cells for Java.Android en tant que bibliothèque. Veuillez choisir correctement et cliquez sur OK.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_11.png)

Vous devez également ajouter le fichier APK au projet. Vous devez copier l'APK dans le dossier **\app\src\main\assets**. Si vous n'avez pas de dossier assets sous le dossier principal, vous pouvez en créer un en cliquant avec le bouton droit sur le nœud principal dans la vue Projet. Sélectionnez Nouveau > Dossier > Dossier d'assets.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_12.png)

Une fois que l'APK a été ajouté au projet, il doit être chargé par le projet. Il existe 2 façons de charger l'APK comme suit.

- Chargez l'APK dans une classe d'application personnalisée en utilisant le fragment fourni ci-dessous et enregistrez la classe d'application personnalisée dans le AndroidManifest.xml.

{{< highlight java >}}

 LibsLoadHelper.loadLibs(this);

{{< /highlight >}}

- Chargez l'APK dans la méthode OnCreate de MainActivity.

{{< highlight java >}}

 LibsLoadHelper.loadLibs(getApplicationContext());

{{< /highlight >}}

Maintenant nous sommes prêts à écrire le code. Afin de rendre la démonstration facile à comprendre, nous avons ajouté un widget Button à la mise en page et allons gérer son événement de clic comme suit.

{{< highlight java >}}

 private class TestTask extends AsyncTask<Void, String, Boolean> {

    @Override

    protected Boolean doInBackground(Void... params) {

        Boolean result = false;

        Workbook book = new Workbook();

        Worksheet sheet = book.getWorksheets().get(0);

        Cells cells = sheet.getCells();

        Cell cell = cells.get("A1");

        cell.putValue("Hello World!");

        try {

            book.save(SD_PATH + "output.xlsx");

        } catch (Exception e) {

            e.printStackTrace();

        }

        return result;

    }

}

{{< /highlight >}}

Lorsque vous exécutez l'application en utilisant le bouton de lecture sur l'interface de l'IDE (ou en utilisant MAJ + F10), l'émulateur chargera l'application comme indiqué ci-dessous.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_13.png)

En cliquant sur le bouton de l'émulateur, le code sera exécuté pour créer une nouvelle feuille de calcul dans le dossier de stockage externe de l'émulateur. Vous pouvez accéder au fichier depuis le Moniteur de périphérique Android comme indiqué ci-dessous.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_14.png)

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_15.png)


