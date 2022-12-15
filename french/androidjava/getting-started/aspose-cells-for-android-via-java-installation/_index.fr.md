---
title: Aspose.Cells for Android via Java Installation
type: docs
weight: 30
url: /fr/java/aspose-cells-for-android-via-java-installation/
---
## **Configuration requise**
Aspose.Cells for Android via Java est indépendant de la plate-forme et peut être utilisé sur n'importe quelle plate-forme sur laquelle l'environnement d'exécution Android est installé et fonctionnera sur les systèmes Android exécutant Android OS 2.0 ou supérieur. À l'heure actuelle, le composant a été testé avec :

- Android 5.1 version 22
## **Installer Aspose.Cells for Android via Java à partir du référentiel Maven**
1. Ajoutez le référentiel maven dans votre build.gradle
1. Ajouter 'Aspose.Cells for Android via Java' JAR comme dépendance

{{< highlight "java" >}}

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
## **Comment utiliser Aspose.Cells for Android via Java**
Cette rubrique vous guidera à travers les étapes nécessaires pour configurer Aspose.Cells for Android via Java dans Android Studio IDE, en supposant que vous avez déjà la dernière version d'Android Studio installée sur votre machine et que vous avez également acquis la dernière version du package Aspose.Cells for Android via Java.

{{% alert color="primary" %}} 

Si vous n'avez pas encore installé Android Studio, vous devez d'abord acquérir la configuration d'Android Studio et l'installer sur votre machine. Vous pouvez télécharger la dernière version d'Android Studio à partir de[ici](https://developer.android.com/studio/index.html#win-bundle) tandis que les détails sur la façon d'installer l'IDE sont disponibles[ici](https://developer.android.com/studio/install.html).

{{% /alert %}} {{% alert color="primary" %}} 

 Le package Aspose.Cells for Android via Java peut être téléchargé à partir de[ici](https://downloads.aspose.com/cells/androidjava). Veuillez noter que chaque package de version de Aspose.Cells for Android via Java se compose principalement de 2 fichiers comme détaillé ci-dessous.

- **aspose-cellules-xxxjar** est le fichier de bibliothèque principal contenant tous les espaces de noms de Aspose.Cells for Android via Java API.
- **aspose-cells-xxx-libs.apk** est l'APK contenant le fichier tiers bcprov-jdk15-146.jar utilisé pour les fonctions de cryptage et de décryptage proposées par Aspose.Cells for Android via Java API.

{{% /alert %}} 
### **Premiers pas avec Aspose.Cells for Android via Java dans Android Studio**
Une fois l'IDE Android Studio chargé, cliquez sur Fichier> Nouveau> Nouveau projet comme indiqué ci-dessous.

![tâche : image_autre_texte](aspose-cells-for-android-via-java-installation_1.png)

Vous pouvez également créer un nouveau projet à partir de l'écran de bienvenue d'Android Studio, comme indiqué ci-dessous.

![tâche : image_autre_texte](aspose-cells-for-android-via-java-installation_2.png)

Ensuite, vous serez invité à spécifier le nom de l'application, le domaine et l'emplacement pour stocker les fichiers du projet. Vous pouvez choisir de modifier les valeurs par défaut selon votre choix ou de les laisser telles quelles, puis de cliquer sur Suivant.

![tâche : image_autre_texte](aspose-cells-for-android-via-java-installation_3.png)

À l'étape suivante, vous devez spécifier l'appareil Android sur lequel vous souhaitez héberger/exécuter votre application. Une fois sélectionné, cliquez sur le bouton Suivant.

![tâche : image_autre_texte](aspose-cells-for-android-via-java-installation_4.png)

Vous devez maintenant sélectionner l'activité dans une liste prédéfinie de modèles. Afin de garder la démonstration simple, nous avons sélectionné le modèle d'activité vide comme indiqué ci-dessous.

![tâche : image_autre_texte](aspose-cells-for-android-via-java-installation_5.png)

Cliquez sur le bouton Terminer dans la boîte de dialogue Personnaliser l'activité car nous conserverons tous les paramètres par défaut tels quels.

![tâche : image_autre_texte](aspose-cells-for-android-via-java-installation_6.png)

Dès que vous cliquez sur le bouton Terminer à l'étape précédente, l'IDE commencera à construire le projet comme indiqué ci-dessous. Laissez-le finir ou cliquez sur le bouton Annuler.

![tâche : image_autre_texte](aspose-cells-for-android-via-java-installation_7.png)

Maintenant que le projet a été chargé dans l'EDI, cependant, vous souhaiterez peut-être changer la vue en Projet afin de pouvoir afficher la hiérarchie complète des fichiers du projet. Afin de changer la vue, veuillez vérifier l'instantané suivant.

![tâche : image_autre_texte](aspose-cells-for-android-via-java-installation_8.png)

 Après avoir changé la vue en projet, recherchez et chargez le**build.gradle** fichier dans l'éditeur et collez l'extrait suivant comme indiqué ci-dessous.

{{< highlight "java" >}}

 dexOptions{

    javaMaxHeapSize "4g"

}

{{< /highlight >}}

![tâche : image_autre_texte](aspose-cells-for-android-via-java-installation_9.png)

Ensuite, nous ajouterons le Jar Aspose.Cells for Android via Java au projet. Il y a 2 étapes importantes comme détaillé ci-dessous.

-  Copiez manuellement le pot Aspose.Cells for Android via Java dans le**\app\libs** dossier.
- Ajoutez Aspose.Cells for Android via Java Jar as Library au module comme indiqué ci-dessous.

![tâche : image_autre_texte](aspose-cells-for-android-via-java-installation_10.png)

Vous serez invité à sélectionner le module auquel vous souhaitez ajouter le Jar Aspose.Cells for Java.Android en tant que bibliothèque. Veuillez choisir de manière appropriée et cliquez sur OK.

![tâche : image_autre_texte](aspose-cells-for-android-via-java-installation_11.png)

 Vous devez également ajouter le fichier APK au projet. Vous devez copier l'APK dans le**\app\src\main\assets**dossier. Si vous n'avez pas le dossier des actifs sous le dossier principal, vous pouvez en créer un en cliquant avec le bouton droit sur le nœud principal dans la vue Projet. Sélectionnez Nouveau > Dossier > Dossier d'actifs.

![tâche : image_autre_texte](aspose-cells-for-android-via-java-installation_12.png)

Une fois l'APK ajouté au projet, il doit être chargé par le projet. Il existe 2 façons de charger l'APK comme suit.

- Chargez l'APK dans une classe d'application personnalisée à l'aide de l'extrait de code fourni ci-dessous et enregistrez la classe d'application personnalisée dans AndroidManifest.xml.

{{< highlight "java" >}}

 LibsLoadHelper.loadLibs(this);

{{< /highlight >}}

- Chargez l'APK dans la méthode OnCreate de MainActivity.

{{< highlight "java" >}}

 LibsLoadHelper.loadLibs(getApplicationContext());

{{< /highlight >}}

Nous sommes maintenant prêts à écrire le code. Afin de garder la démonstration facile à comprendre, nous avons ajouté un widget Button à la mise en page et allons gérer son événement de clic comme suit.

{{< highlight "java" >}}

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

Lorsque vous exécutez l'application à l'aide du bouton de lecture sur l'interface IDE (ou à l'aide de SHIFT + F10), l'émulateur charge l'application comme indiqué ci-dessous.

![tâche : image_autre_texte](aspose-cells-for-android-via-java-installation_13.png)

Cliquer sur le bouton de l'émulateur exécutera le code pour créer une nouvelle feuille de calcul dans le dossier de stockage externe de l'émulateur. Vous pouvez accéder au fichier depuis Android Device Monitor comme indiqué ci-dessous.

![tâche : image_autre_texte](aspose-cells-for-android-via-java-installation_14.png)

![tâche : image_autre_texte](aspose-cells-for-android-via-java-installation_15.png)


