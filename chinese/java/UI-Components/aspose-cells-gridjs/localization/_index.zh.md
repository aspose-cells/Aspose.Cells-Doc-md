---
title: GridJs 多语言配置指南
type: docs
weight: 250
url: /zh/java/aspose-cells-gridjs/how-to-configuration-multi-language/
description: 本教程将引导您配置多语言支持
keywords: GridJs、多语言、本地化、国际化、文化、CultureInfo
aliases:
- /java/aspose-cells-gridjs/multi-language/
- /java/aspose-cells-gridjs/multi-language-guide/
- /java/aspose-cells-gridjs/localization-setup/
- /java/aspose-cells-gridjs/multi-language-configuration/
- /java/aspose-cells-gridjs/internationalization-guide/
- /java/aspose-cells-gridjs/culture-configuration/
---

# Aspose.Cells GridJs 多语言配置指南

## 概述

本教程将引导您在 Aspose.Cells GridJs 项目中配置多语言支持。涵盖前端和后端配置内容。

本教程基于 [演示项目](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/main/Examples.GridJs)，请根据实际情况调整

## 前端配置

在您的前端页面中，使用 [选项](https://docs.aspose.com/cells/net/aspose-cells-gridjs/how-to-use-gridjs-client-api/) 设置界面语言为 `local`

在演示项目中，您需要修改 [uidload.html](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/main/Examples.GridJs/src/main/resources/templates/index.html) 文件

以下是一个例子：

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

## 后端配置

在后端代码中，处理Excel数据前需要设置合适的 CultureInfo。

在演示项目中，您需要修改 [Application](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/main/Examples.GridJs/src/main/java/com/aspose/gridjs/demo/GridjsdemoApplication.java) 文件

### 在 main 方法中设置区域设置

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

## 重要说明

1. 前端和后端的语言设置必须一致。
2. 在处理Excel数据之前，必须设置CultureInfo。
3. 支持的语言：en（英语）、zh（中文）、es（西班牙语）、pt（葡萄牙语）、de（德语）、ru（俄语）、nl（荷兰语）、pl（波兰语）。
4. 示例使用波兰语（pl-PL），但可以更改为其他支持的区域设置。
