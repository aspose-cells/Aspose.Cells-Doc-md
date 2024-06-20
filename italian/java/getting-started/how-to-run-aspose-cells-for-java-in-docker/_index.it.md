---
title: Come eseguire Aspose.Cells for Java in Docker
type: docs
description: "Esegui Aspose.Cells for Java in un contenitore Docker per Linux."
weight: 139
url: /it/java/how-to-run-aspose-cells-in-docker/
---

I microservizi, in combinazione con la containerizzazione, rendono possibile combinare facilmente le tecnologie. Docker ti consente di integrare facilmente la funzionalità Aspose.Cells nella tua applicazione, indipendentemente dalla tecnologia utilizzata nel tuo stack di sviluppo.

Nel caso in cui stai puntando ai microservizi, o se la principale tecnologia nel tuo stack non è .NET, C++ o Java, ma hai bisogno della funzionalità di Aspose.Cells, o se già utilizzi Docker nel tuo stack, potresti essere interessato a utilizzare Aspose.Cells for Java in un contenitore Docker.

## Prerequisiti

- Docker deve essere installato sul tuo sistema. 

## Creare un'applicazione Java

In questo esempio, creerai un'applicazione Java che crea un semplice file xlsx, lo salva e lo legge. L'applicazione può quindi essere compilata ed eseguita in Docker.

### Creazione dell'applicazione Java

Crea l'applicazione Java in Eclipse utilizzando il codice seguente. In questo esempio, utilizziamo Aspose.Cells for Java per creare un nuovo foglio di lavoro xlsx e impostiamo il nome del foglio e i valori delle celle, quindi li leggiamo e li visualizziamo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "TestDocker.java" >}}

### Creare l'applicazione Java in un pacchetto jar

Nella figura seguente viene mostrato un modo per creare un pacchetto jar utilizzando il menu "Esporta" in Eclipse.

**![Creare Jar utilizzando Eclipse](MakeJar.png)**

Ora che abbiamo scritto un programma Java utilizzando Aspose.Cells for Java, abbiamo ottenuto un pacchetto jar. Ora faremo un dockerfile.

### Configurare un file Dockerfile

Il passo successivo è creare e configurare il Dockerfile.

1. Crea il Dockerfile e posizionalo accanto al pacchetto jar. Mantieni lo stesso nome del file senza estensione (predefinito).
2. Nel Dockerfile, specifica:

{{< highlight plain >}}
   FROM williamyeh/java8:latest

   VOLUME /tmp

   ADD TestDocker.jar app.jar

   ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
{{< /highlight >}}

### Costruzione ed Esecuzione dell'Applicazione in Docker

Ora l'applicazione può essere costruita ed eseguita in Docker. Apri il tuo prompt dei comandi preferito, cambia directory nella cartella con il Dockerfile ed esegui il seguente comando:

{{< highlight plain >}}
docker build -t java-app .
{{< /highlight >}}

Dopo aver eseguito il comando sopra, otterrai l'output del foglio di calcolo XLSX e il risultato della riga di comando. A questo punto, un programma Java è stato eseguito con successo in Linux Docker.
