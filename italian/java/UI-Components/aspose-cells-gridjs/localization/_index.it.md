---
title: Guida alla configurazione multi lingua di GridJs
type: docs
weight: 250
url: /it/java/aspose-cells-gridjs/how-to-configuration-multi-language/
description: Questa guida ti aiuterà a configurare il supporto multilingue
keywords: GridJs, multilingue, localizzazione, internazionalizzazione, cultura, CultureInfo
aliases:
- /java/aspose-cells-gridjs/multi-language/
- /java/aspose-cells-gridjs/multi-language-guide/
- /java/aspose-cells-gridjs/localization-setup/
- /java/aspose-cells-gridjs/multi-language-configuration/
- /java/aspose-cells-gridjs/internationalization-guide/
- /java/aspose-cells-gridjs/culture-configuration/
---

# Guida alla configurazione multilingue di Aspose.Cells GridJs

## Panoramica

Questa guida ti guiderà nella configurazione del supporto multilingue nel tuo progetto Aspose.Cells GridJs. Copre sia le configurazioni frontend che backend.

Il tutorial è basato sul [progetto demo](https://github.com/aspose-cells/Aspose.Cells/Grid-for-Java/tree/main/Examples.GridJs), si prega di adattarlo alla situazione reale

## Configurazione frontend

Nei tuoi frontend, imposta la lingua dell'interfaccia usando l'[opzione](https://docs.aspose.com/cells/net/aspose-cells-gridjs/how-to-use-gridjs-client-api/).

Nel progetto demo, è necessario modificare il file [uidload.html](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/main/Examples.GridJs/src/main/resources/templates/index.html)

Ecco un esempio:

```javascript
const loadNormalContext = (sheet) => {
    const option = {
        updateMode: 'server',
        updateUrl: '/GridJs2/UpdateCell',
        showToolbar: true,
        mode: 'edit',
        // Supported languages: en/zh/es/pt/de/ru/nl/pl
        local: 'pl', // Set to Polish in this example
    };
    loadWithOption(jsondata, option);
};
```

## Configurazione backend

Nel codice backend, è necessario impostare CultureInfo appropriato prima di elaborare i dati Excel.

Nel progetto demo, è necessario modificare il file [Application](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/main/Examples.GridJs/src/main/java/com/aspose/gridjs/demo/GridjsdemoApplication.java)

### impostare le impostazioni della lingua nel metodo main

```java

public static void main(String[] args) {

	// Set Polish locale for current thread
        Locale polishLocale = new Locale("pl", "PL");
        Locale.setDefault(polishLocale);

        // Demonstration of locale settings
        System.out.println("Current Locale: " + Locale.getDefault());

		 ApplicationContext context  = 	SpringApplication.run(GridjsdemoApplication.class, args);

		 MyConfig myConfig = context.getBean(MyConfig.class);

		 //set license for Aspose.Cells
		 com.aspose.cells.License  lic=new com.aspose.cells.License();
			if ((new File(myConfig.asposeLicensePath)).exists()) {
				lic.setLicense(myConfig.asposeLicensePath);
			}


	}

```

## Note importanti

1. Le impostazioni della lingua frontend e backend devono essere coerenti.
2. CultureInfo deve essere impostato prima di elaborare i dati Excel.
3. Lingue supportate: en(inglese), zh(cinese), es(spagnolo), pt(portoghese), de(tedesco), ru(russo), nl(olandese), pl(polacco).
4. L'esempio utilizza il polacco (pl-PL), ma puoi cambiarlo in qualsiasi altra locale supportata.
