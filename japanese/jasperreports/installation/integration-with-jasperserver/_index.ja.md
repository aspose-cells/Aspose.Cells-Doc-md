---
title: JasperServer との統合
type: docs
weight: 30
url: /ja/jasperreports/integration-with-jasperserver/
---
{{% alert color="primary" %}} 

Aspose.Cells for JasperReports を JasperServer と統合するには、次の手順を実行します。

{{% /alert %}} 

{{% alert color="primary" %}} 

以下のすべての手順で<InstallDir>は、JasperServer インストール ディレクトリを表します。

{{% /alert %}} 

1. 次の新しいエクスポーター プロパティを**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml**ファイル。

**XML**

{{< highlight "csharp" >}}

 <bean id="reportACXlsExporter" class="com.aspose.cells.jasperreports.ACReportXlsExporter" parent="baseReportExporter">

   <property name="exportParameters" ref="excelACExportParameters"/>

   <property name="setResponseContentLength" value="true"/>

</bean>

<bean id="xlsACExporterConfiguration" class="com.jaspersoft.jasperserver.war.action.ExporterConfigurationBean">

   <property name="descriptionKey" value="XLS - Excel Presentation via Aspose.Cells"/>

   <property name="iconSrc" value="/images/xls.gif"/>

   <property name="parameterDialogName" value="excelACExportParams"/>

   <property name="exportParameters" ref="excelACExportParameters"/>

   <property name="currentExporter" ref="reportACXlsExporter"/>

</bean>



{{< /highlight >}}

1. を見つけます<util:map id=”exporterConfigMap>の要素**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml**ファイルに次の行を追加します。

**XML**

{{< highlight "csharp" >}}

 <util:map id="exporterConfigMap">

   <entry key="pdf" value-ref="pdfExporterConfiguration"/>

   <entry key="xls" value-ref="xlsExporterConfiguration"/>

   <entry key="rtf" value-ref="rtfExporterConfiguration"/>

   <entry key="csv" value-ref="csvExporterConfiguration"/>

   <entry key="swf" value-ref="swfExporterConfiguration"/>

<!-- START of ADDED LINES -->

   <entry key="xls" value-ref="xlsACExporterConfiguration"/>

<!-- END of NEW LINES -->

</util:map>



{{< /highlight >}}




1. からすべての GIF 画像をコピーします。**\lib**フォルダ内の**aspose.cells.jasperreports.zip**に*<InstallDir>\apache-tomcat\webapps\jasperserver\images*フォルダ。
1. コピー**aspose.cells.jasperreports.jar**からのファイル**\lib**フォルダ内の**aspose.cells.jasperreports.zip**に**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\lib\.**フォルダ。
1. 次の行を**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml**ファイル。
 (この Bean には、エクスポートを構成するためのさまざまな構成設定が含まれている場合があります。たとえば、JasperReports フォント マッピング機能を使用したり、Aspose.Cells for JasperReports ライセンス ファイルの場所を指定したりできます。)

**XML**

{{< highlight "csharp" >}}

 <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean"> <!-- Uncomment to apply a license. Check the license path.

<property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

-->

</bean>



{{< /highlight >}}




1. JasperServer を実行し、任意のレポートを開いて表示します。前の手順が適切に実行された場合は、追加の形式アイコンを使用できます。

**JasperServer に Aspose.Cells for JasperReports をインストールすると、新しいエクスポート形式が利用可能になります (右側)。** 

![todo:画像_代替_文章](integration-with-jasperserver_1.png)



