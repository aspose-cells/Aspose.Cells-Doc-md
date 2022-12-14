---
title: Aspose.Cells per Android tramite installazione Java
type: docs
weight: 30
url: /it/java/aspose-cells-for-android-via-java-installation/
---
## **Requisiti di sistema**
Aspose.Cells per Android tramite Java è indipendente dalla piattaforma e può essere utilizzato su qualsiasi piattaforma in cui è installato l'ambiente Android Runtime e verrà eseguito su sistemi Android con sistema operativo Android 2.0 o versioni successive. Attualmente il componente è stato testato con:

- Android 5.1 versione 22
## **Installa Aspose.Cells per Android tramite Java dal repository Maven**
1. Aggiungi il repository maven al tuo build.gradle
1. Aggiungi "Aspose.Cells per Android tramite Java" JAR come dipendenza

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
## **Come utilizzare Aspose.Cells per Android tramite Java**
Questo argomento ti guiderà attraverso i passaggi necessari per configurare Aspose.Cells per Android tramite Java in Android Studio IDE, supponendo che tu abbia già l'ultima versione di Android Studio installata sul tuo computer e che tu abbia anche acquisito l'ultima versione di Aspose.Cells per Android tramite Java pacchetto.

{{% alert color="primary" %}} 

Se non hai ancora installato Android Studio, devi prima acquisire la configurazione di Android Studio e installarlo sulla tua macchina. Puoi scaricare l'ultima versione di Android Studio da[qui](https://developer.android.com/studio/index.html#win-bundle) mentre i dettagli su come installare l'IDE sono disponibili[qui](https://developer.android.com/studio/install.html).

{{% /alert %}} {{% alert color="primary" %}} 

 Aspose.Cells per Android tramite il pacchetto Java scaricabile da[qui](https://downloads.aspose.com/cells/androidjava). Si prega di notare che ogni pacchetto di rilascio di Aspose.Cells per Android tramite Java consiste principalmente di 2 file come descritto di seguito.

- **aspose-cells-xxxjar** è il file della libreria principale contenente tutti gli spazi dei nomi da Aspose.Cells per Android tramite Java API.
- **aspose-cells-xxx-libs.apk** è l'APK contenente il bcprov-jdk15-146.jar di terze parti utilizzato per le strutture di crittografia e decrittografia offerte da Aspose.Cells per Android tramite Java API.

{{% /alert %}} 
### **Guida introduttiva a Aspose.Cells per Android tramite Java in Android Studio**
Una volta caricato l'IDE di Android Studio, fai clic su File> Nuovo> Nuovo progetto come mostrato di seguito.

![cose da fare:immagine_alt_testo](aspose-cells-for-android-via-java-installation_1.png)

Puoi anche creare un nuovo progetto dalla schermata di benvenuto di Android Studio, come mostrato di seguito.

![cose da fare:immagine_alt_testo](aspose-cells-for-android-via-java-installation_2.png)

Successivamente, ti verrà richiesto di specificare il nome dell'applicazione, il dominio e la posizione per archiviare i file di progetto. Puoi scegliere di modificare i valori predefiniti secondo la tua scelta o lasciarli così come sono e fare clic su Avanti.

![cose da fare:immagine_alt_testo](aspose-cells-for-android-via-java-installation_3.png)

Nel passaggio successivo, devi specificare il dispositivo Android che desideri ospitare/eseguire la tua applicazione. Una volta selezionato, fare clic sul pulsante Avanti.

![cose da fare:immagine_alt_testo](aspose-cells-for-android-via-java-installation_4.png)

Ora devi selezionare l'attività da un elenco predefinito di modelli. Per semplificare la dimostrazione, abbiamo selezionato il modello Attività vuota come mostrato di seguito.

![cose da fare:immagine_alt_testo](aspose-cells-for-android-via-java-installation_5.png)

Fare clic sul pulsante Fine nella finestra di dialogo Personalizza l'attività poiché manterremo tutte le impostazioni predefinite così come sono.

![cose da fare:immagine_alt_testo](aspose-cells-for-android-via-java-installation_6.png)

Non appena si fa clic sul pulsante Fine nel passaggio precedente, l'IDE inizierà a creare il progetto come mostrato di seguito. Lascia che finisca o fai clic sul pulsante Annulla.

![cose da fare:immagine_alt_testo](aspose-cells-for-android-via-java-installation_7.png)

Ora che il progetto è stato caricato nell'IDE, tuttavia, potresti voler modificare la visualizzazione in Project in modo da poter visualizzare la gerarchia completa dei file di progetto. Per cambiare la visualizzazione, controlla la seguente istantanea.

![cose da fare:immagine_alt_testo](aspose-cells-for-android-via-java-installation_8.png)

 Dopo aver cambiato la vista in Project, trova e carica il file**build.gradle** file nell'editor e incolla il seguente frammento come mostrato di seguito.

{{< highlight "java" >}}

 dexOptions{

    javaMaxHeapSize "4g"

}

{{< /highlight >}}

![cose da fare:immagine_alt_testo](aspose-cells-for-android-via-java-installation_9.png)

Successivamente, aggiungeremo Aspose.Cells per Android tramite Java Jar al progetto. Ci sono 2 passaggi importanti come descritto di seguito.

-  Copia manualmente Aspose.Cells per Android tramite Java Jar nel**\app\libs** cartella.
- Aggiungi Aspose.Cells per Android tramite Java Jar come libreria al modulo come mostrato di seguito.

![cose da fare:immagine_alt_testo](aspose-cells-for-android-via-java-installation_10.png)

Ti verrà chiesto di selezionare il modulo a cui desideri aggiungere Aspose.Cells for Java.Android Jar come libreria. Si prega di scegliere in modo appropriato e fare clic su OK.

![cose da fare:immagine_alt_testo](aspose-cells-for-android-via-java-installation_11.png)

 Devi anche aggiungere il file APK al progetto. Devi copiare l'APK nel file**\app\src\main\assets**cartella. Se non hai la cartella delle risorse nella cartella principale, puoi crearne una facendo clic con il pulsante destro del mouse sul nodo principale nella vista Progetto. Selezionare Nuovo > Cartella > Cartella risorse.

![cose da fare:immagine_alt_testo](aspose-cells-for-android-via-java-installation_12.png)

Una volta che l'APK è stato aggiunto al progetto, deve essere caricato dal progetto. Ci sono 2 modi per caricare l'APK come segue.

- Carica l'APK in una classe di applicazione personalizzata utilizzando lo snippet fornito di seguito e registra la classe di applicazione personalizzata in AndroidManifest.xml.

{{< highlight "java" >}}

 LibsLoadHelper.loadLibs(this);

{{< /highlight >}}

- Carica l'APK nel metodo OnCreate di MainActivity.

{{< highlight "java" >}}

 LibsLoadHelper.loadLibs(getApplicationContext());

{{< /highlight >}}

Ora siamo pronti per scrivere il codice. Per mantenere la dimostrazione facile da capire, abbiamo aggiunto un widget Button al layout e gestiremo il suo evento click come segue.

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

Quando si esegue l'applicazione utilizzando il pulsante di riproduzione sull'interfaccia IDE (o utilizzando SHIFT + F10) l'emulatore caricherà l'applicazione come mostrato di seguito.

![cose da fare:immagine_alt_testo](aspose-cells-for-android-via-java-installation_13.png)

Facendo clic sul pulsante sull'emulatore verrà eseguito il codice per creare un nuovo foglio di calcolo nella cartella di archiviazione esterna dell'emulatore. Puoi accedere al file da Android Device Monitor come mostrato di seguito.

![cose da fare:immagine_alt_testo](aspose-cells-for-android-via-java-installation_14.png)

![cose da fare:immagine_alt_testo](aspose-cells-for-android-via-java-installation_15.png)


