---
title: ライセンス
type: docs
weight: 40
url: /ja/jasperreports/licensing/
---
{{% alert color="primary" %}}

 Aspose.Cells for JasperReports は、[ダウンロードページ](https://downloads.aspose.com/cells/jasperreports).製品の評価版とライセンス版は同じダウンロードです。

評価版に満足したら、[ライセンスを購入する](https://purchase.aspose.com/).ライセンス条項を理解し、同意してください。

ライセンスは、注文の支払いが完了すると、注文ページからダウンロードできます。ライセンスは、デジタル署名されたクリア テキストの XML ファイルです。ライセンスには、クライアント名、購入した製品、ライセンスの種類などの情報が含まれています。ライセンス ファイルの内容を変更しないでください。変更すると、ライセンスが無効になります。

ライセンスを適用するには、次の 2 つの方法があります。

- [setLicense を呼び出す](/cells/ja/jasperreports/licensing/#call-setlicense)
- [applicationContext.xml でエクスポーター パラメーターを設定する](/cells/ja/jasperreports/licensing/#set-the-licensefile-exporter-parameter-in-applicationcontextxml)

ライセンスをインストールしたら、

- [動作することを確認する](/cells/ja/jasperreports/licensing/#verify-the-license-works).

{{% /alert %}}

## **setLicense を呼び出す**

{{% alert color="primary" %}}

このメソッドは、JasperReports での使用に適用できます。

{{% /alert %}}

ライセンスをコンピュータにダウンロードし、適切なフォルダ (アプリケーションのフォルダや**JasperReports\lib**).
プロジェクトに次のコードを追加します。

{{< highlight "csharp" >}}

import com.aspose.cells.jasperreports.*;

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream("C:\\Aspose.Cells.JasperReports.lic");

// Set the license through the stream object

License license = new License();

license.setLicense(fstream);

{{< /highlight >}}

## **applicationContext.xml で licenseFile エクスポーター パラメーターを設定します。**

{{% alert color="primary" %}}

このメソッドは、JasperServer での使用に適用できます。

{{% /alert %}}

1. ライセンスをコンピュータにダウンロードし、**\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF**フォルダ、場所**\<インストールディレクトリ>**は、JasperServer インストール ディレクトリを表します。
1. を見つけます**\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml**ファイルに次の行を追加します。

**XML**

{{< highlight "csharp" >}}

  <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

</bean>

{{< /highlight >}}

## **ライセンスの動作確認**

レポートを XLS 形式にエクスポートし、レポートに評価メッセージが含まれているかどうかを確認します。評価メッセージがない場合、ライセンスは正常に機能しています。

**Aspose.Cells for JasperReports 評価モードで評価ワークシートを挿入します** 

![todo:画像_代替_文章](licensing_1.png)

**有効なライセンスの場合、評価ワークシートはありません** 

![todo:画像_代替_文章](licensing_2.png)
