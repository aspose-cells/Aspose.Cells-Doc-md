---
title: GridJs Multi-Language Configuration Guide
type: docs
weight: 250
url: /java/aspose-cells-gridjs/how-to-configuration-multi-language/
description: This tutorial will guide you through configuring multi-language support
keywords: GridJs, multi-language, localization, internationalization, culture, CultureInfo
aliases:
- /java/aspose-cells-gridjs/multi-language/
- /java/aspose-cells-gridjs/multi-language-guide/
- /java/aspose-cells-gridjs/localization-setup/
- /java/aspose-cells-gridjs/multi-language-configuration/
- /java/aspose-cells-gridjs/internationalization-guide/
- /java/aspose-cells-gridjs/culture-configuration/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# Aspose.Cells GridJs Multi-Language Configuration Guide

## Overview

This tutorial will guide you through configuring multi-language support in your Aspose.Cells GridJs project. It covers both frontend and backend configurations.

The tutorial is based on the [demo project](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/main/Examples.GridJs), please adjust according to the actual situation

## Frontend Configuration

In your frontend pages, set the interface language using the `local` [option](https://docs.aspose.com/cells/net/aspose-cells-gridjs/how-to-use-gridjs-client-api/).

In the demo project, you need to modify the [uidload.html](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/main/Examples.GridJs/src/main/resources/templates/index.html) file

Here's an example:

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

## Backend Configuration

In the backend code, you need to set the appropriate CultureInfo before processing Excel data.

In the demo project, you need to modify the [Application](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/main/Examples.GridJs/src/main/java/com/aspose/gridjs/demo/GridjsdemoApplication.java) file

### set locale settings in main method
 
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

## Important Notes

1. Frontend and backend language settings must be consistent.
2. CultureInfo must be set before processing Excel data.
3. Supported languages: en(English), zh(Chinese), es(Spanish), pt(Portuguese), de(German), ru(Russian), nl(Dutch), pl(Polish).
4. The example uses Polish (pl-PL), but you can change it to any other supported locale.
