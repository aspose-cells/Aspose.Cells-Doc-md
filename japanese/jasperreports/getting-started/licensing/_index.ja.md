---
title: ライセンス
type: docs
weight: 40
url: /ja/jasperreports/licensing/
---

{{% alert color="primary" %}}

Aspose.Cells for JasperReportsは、[ダウンロードページ](https://downloads.aspose.com/cells/jasperreports)から無料で時間制限のない評価版として利用できます。製品の評価版とライセンス版のダウンロードは同じです。

評価版に満足したら、[ライセンスを購入](https://purchase.aspose.com/)することができます。ライセンス規約を理解し、同意することを確認してください。

注文が支払われた後、注文ページからライセンスをダウンロードできます。ライセンスはクライアント名、購入製品、ライセンスタイプなどの情報を含む、明瞭なテキストでデジタルに署名されたXMLファイルです。ライセンスファイルの内容を変更しないでください。これはライセンスを無効にします。

ライセンスを適用する方法には2つの方法があります:

- [setLicenseを呼び出す](/cells/ja/jasperreports/licensing/#call-setlicense)
- [applicationContext.xmlでエクスポーターパラメーターを設定する](/cells/ja/jasperreports/licensing/#set-the-licensefile-exporter-parameter-in-applicationcontextxml)

ライセンスをインストールした後、

- [動作を確認します](/cells/ja/jasperreports/licensing/#verify-the-license-works)。

{{% /alert %}}

## **setLicenseを呼び出す**

{{% alert color="primary" %}}

このメソッドはJasperReportsと使用するために適用可能です。

{{% /alert %}}

ライセンスをコンピューターにダウンロードし、適切なフォルダーにコピーします（たとえばアプリケーションのフォルダーまたは **JasperReports\lib** など）。
以下のコードをプロジェクトに追加します。

{{< highlight csharp >}}

import com.aspose.cells.jasperreports.*;

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream("C:\\Aspose.Cells.JasperReports.lic");

// Set the license through the stream object

License license = new License();

license.setLicense(fstream);

{{< /highlight >}}

## **applicationContext.xmlでlicenseFileエクスポーターパラメーターを設定します**

{{% alert color="primary" %}}

このメソッドはJasperServerと使用するために適用可能です。

{{% /alert %}}

1. Download the license to your computer and copy it to the **\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF** folder, where **\<InstallDir>** stands for the JasperServer installation directory.
1. Locate the **\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** file and add the following lines:

**XML**

{{< highlight csharp >}}

  <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

</bean>

{{< /highlight >}}

## **ライセンスが正常に動作しているか確認します**

任意のレポートをXLS形式でエクスポートし、レポートに評価メッセージが含まれているかどうかを確認します。 評価メッセージがない場合、ライセンスは正常に動作しています。

**Aspose.Cells for JasperReportsは評価ワークシートを評価モードで注入します** 

![todo:image_alt_text](licensing_1.png)

**有効なライセンスがあるときに評価ワークシートは表示されません** 

![todo:image_alt_text](licensing_2.png)
