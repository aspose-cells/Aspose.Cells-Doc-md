---
title: Installazione di Aspose.Cells per Android via Java
type: docs
weight: 30
url: /it/java/aspose-cells-for-android-via-java-installation/
---

## **Requisiti di sistema**
Aspose.Cells per Android via Java è indipendente dalla piattaforma e può essere utilizzato su qualsiasi piattaforma dove è installato l'ambiente di esecuzione Android e funzionerà su sistemi Android con sistema operativo Android 2.0 o superiore. Attualmente, il componente è stato testato con:

- Android 5.1 v 22
## **Installa Aspose.Cells per Android via Java dal repository Maven**
1. Aggiungi il repository maven nel tuo build.gradle 
1. Aggiungi 'Aspose.Cells per Android via Java' JAR come dipendenza

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

    compile (group: 'com.aspose', name: 'aspose-cells', version: '25.9', classifier: 'android.via.java')

}

{{< /highlight >}}
## **Come utilizzare Aspose.Cells per Android via Java**
Questo argomento ti guiderà attraverso i passi necessari per configurare Aspose.Cells per Android via Java in Android Studio IDE, presumendo che tu abbia già installato l'ultima versione di Android Studio sul tuo computer e che tu abbia anche acquisito l'ultima versione del pacchetto Aspose.Cells per Android via Java.

{{% alert color="primary" %}} 

Se non hai ancora installato Android Studio, devi prima acquisire il setup di Android Studio e installarlo sul tuo computer. Puoi scaricare l'ultima versione di Android Studio da [qui](https://developer.android.com/studio/index.html#win-bundle) mentre i dettagli su come installare l'IDE sono disponibili [qui](https://developer.android.com/studio/install.html).

{{% /alert %}} {{% alert color="primary" %}} 

Il pacchetto Aspose.Cells per Android via Java può essere scaricato da [qui](https://downloads.aspose.com/cells/androidjava). Si prega di notare, ciascun pacchetto di rilascio di Aspose.Cells per Android via Java consiste principalmente di 2 file come dettagliato di seguito.

- **aspose-cells-x.x.x.jar** è il file della libreria principale contenente tutti gli spazi dei nomi dall'API Aspose.Cells per Android via Java.
- **aspose-cells-x.x.x-libs.apk** è l'APK contenente il bcprov-jdk15-146.jar di terze parti utilizzato per le funzionalità di crittografia e decrittografia offerte dall'API Aspose.Cells per Android via Java.

{{% /alert %}} 
### **Iniziare con Aspose.Cells per Android via Java in Android Studio**
Una volta caricato l'IDE di Android Studio, fai clic su File > Nuovo > Nuovo Progetto come mostrato di seguito.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_1.png)

Puoi anche creare un nuovo progetto dalla Schermata di Benvenuto di Android Studio come mostrato di seguito.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_2.png)

Successivamente, ti verrà chiesto di specificare il nome dell'applicazione, il dominio e la posizione per memorizzare i file del progetto. Puoi scegliere di modificare i valori predefiniti come desideri o lasciarli come sono e fare clic su Avanti.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_3.png)

Nel passaggio successivo, devi specificare il Dispositivo Android su cui desideri ospitare/eseguire la tua applicazione. Una volta selezionato, fai clic sul pulsante Avanti.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_4.png)

Ora devi selezionare l'Activity da un elenco predefinito di modelli. Per mantenere la dimostrazione semplice, abbiamo selezionato il modello Empty Activity come mostrato di seguito.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_5.png)

Fai clic sul pulsante Fine nella finestra di Personalizzazione dell'Activity poiché manterremo tutte le impostazioni predefinite come sono.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_6.png)

Non appena fai clic sul pulsante Fine nel passaggio precedente, l'IDE inizierà a creare il progetto come mostrato di seguito. Lascialo finire o fai clic sul pulsante Annulla.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_7.png)

Ora il progetto è stato caricato nell'IDE, tuttavia, potresti desiderare cambiare la visualizzazione in Progetto in modo da poter visualizzare l'intera gerarchia dei file del progetto. Per cambiare la visualizzazione, controlla la seguente schermata.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_8.png)

Dopo aver cambiato la visualizzazione in Progetto, trova e carica il file **build.gradle** nell'editor e incolla il seguente snippet come mostrato di seguito.

{{< highlight java >}}

 dexOptions{

    javaMaxHeapSize "4g"

}

{{< /highlight >}}

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_9.png)

Successivamente, aggiungeremo l'Aspose.Cells per Android via Java Jar al progetto. Ci sono 2 passaggi importanti come dettagliato di seguito.

- Copia manualmente l'Aspose.Cells per Android via Java Jar nella cartella **\app\libs**.
- Aggiungi l'Aspose.Cells per Android via Java Jar come libreria al modulo come mostrato di seguito.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_10.png)

Ti verrà chiesto di selezionare il modulo a cui desideri aggiungere l'Aspose.Cells for Java.Android Jar come libreria. Si prega di scegliere appropriatamente e fare clic su OK.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_11.png)

È anche necessario aggiungere il file APK al progetto. Devi copiare l'APK nella cartella **\app\src\main\assets**. Se non hai la cartella assets sotto la cartella principale, puoi crearne una facendo clic con il pulsante destro del mouse sul nodo principale nella visualizzazione del progetto. Seleziona Nuovo > Cartella > Cartella Asset.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_12.png)

Una volta che l'APK è stato aggiunto al progetto, deve essere caricato dal progetto. Ci sono 2 modi per caricare l'APK come segue.

- Carica l'APK in una classe di applicazione personalizzata utilizzando lo snippet fornito di seguito e registra la classe di applicazione personalizzata nel file AndroidManifest.xml.

{{< highlight java >}}

 LibsLoadHelper.loadLibs(this);

{{< /highlight >}}

- Carica l'APK nel metodo OnCreate di MainActivity.

{{< highlight java >}}

 LibsLoadHelper.loadLibs(getApplicationContext());

{{< /highlight >}}

Ora siamo pronti a scrivere il codice. Per mantenere la dimostrazione facile da capire, abbiamo aggiunto un widget Button al layout e gestiremo il suo evento di clic come segue.

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

Quando si esegue l'applicazione utilizzando il pulsante di riproduzione sull'interfaccia IDE (o utilizzando SHIFT + F10), l'emulatore caricherà l'applicazione come mostrato di seguito.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_13.png)

Cliccando il pulsante sull'emulatore eseguirà il codice per creare un nuovo foglio elettronico nella cartella di memorizzazione esterna dell'emulatore. È possibile accedere al file dal Monitor Dispositivi Android come mostrato di seguito.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_14.png)

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_15.png)


