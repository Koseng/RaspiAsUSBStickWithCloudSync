namespace DropboxAppData
{
    partial class Main
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.textBoxAppKey = new System.Windows.Forms.TextBox();
            this.labelKey = new System.Windows.Forms.Label();
            this.labelSecret = new System.Windows.Forms.Label();
            this.textBoxAppSecret = new System.Windows.Forms.TextBox();
            this.groupBoxInput = new System.Windows.Forms.GroupBox();
            this.label3 = new System.Windows.Forms.Label();
            this.buttonAccessCode = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.label4 = new System.Windows.Forms.Label();
            this.textBoxRefreshToken = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.buttonRefreshToken = new System.Windows.Forms.Button();
            this.textBoxAccessCode = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.groupBoxInput.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // textBoxAppKey
            // 
            this.textBoxAppKey.Location = new System.Drawing.Point(100, 29);
            this.textBoxAppKey.Name = "textBoxAppKey";
            this.textBoxAppKey.Size = new System.Drawing.Size(178, 20);
            this.textBoxAppKey.TabIndex = 0;
            // 
            // labelKey
            // 
            this.labelKey.AutoSize = true;
            this.labelKey.Location = new System.Drawing.Point(36, 32);
            this.labelKey.Name = "labelKey";
            this.labelKey.Size = new System.Drawing.Size(50, 13);
            this.labelKey.TabIndex = 1;
            this.labelKey.Text = "App Key:";
            // 
            // labelSecret
            // 
            this.labelSecret.AutoSize = true;
            this.labelSecret.Location = new System.Drawing.Point(23, 73);
            this.labelSecret.Name = "labelSecret";
            this.labelSecret.Size = new System.Drawing.Size(63, 13);
            this.labelSecret.TabIndex = 2;
            this.labelSecret.Text = "App Secret:";
            // 
            // textBoxAppSecret
            // 
            this.textBoxAppSecret.Location = new System.Drawing.Point(100, 71);
            this.textBoxAppSecret.Name = "textBoxAppSecret";
            this.textBoxAppSecret.Size = new System.Drawing.Size(178, 20);
            this.textBoxAppSecret.TabIndex = 3;
            // 
            // groupBoxInput
            // 
            this.groupBoxInput.Controls.Add(this.label3);
            this.groupBoxInput.Controls.Add(this.buttonAccessCode);
            this.groupBoxInput.Controls.Add(this.textBoxAppKey);
            this.groupBoxInput.Controls.Add(this.textBoxAppSecret);
            this.groupBoxInput.Controls.Add(this.labelKey);
            this.groupBoxInput.Controls.Add(this.labelSecret);
            this.groupBoxInput.Location = new System.Drawing.Point(44, 29);
            this.groupBoxInput.Name = "groupBoxInput";
            this.groupBoxInput.Size = new System.Drawing.Size(355, 184);
            this.groupBoxInput.TabIndex = 4;
            this.groupBoxInput.TabStop = false;
            this.groupBoxInput.Text = "STEP 1";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(81, 153);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(230, 13);
            this.label3.TabIndex = 5;
            this.label3.Text = "Follow steps in browser and copy access code.";
            // 
            // buttonAccessCode
            // 
            this.buttonAccessCode.Location = new System.Drawing.Point(102, 115);
            this.buttonAccessCode.Name = "buttonAccessCode";
            this.buttonAccessCode.Size = new System.Drawing.Size(176, 23);
            this.buttonAccessCode.TabIndex = 4;
            this.buttonAccessCode.Text = "Get Access Code";
            this.buttonAccessCode.UseVisualStyleBackColor = true;
            this.buttonAccessCode.Click += new System.EventHandler(this.buttonAccessCode_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.label4);
            this.groupBox1.Controls.Add(this.textBoxRefreshToken);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.buttonRefreshToken);
            this.groupBox1.Controls.Add(this.textBoxAccessCode);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Location = new System.Drawing.Point(44, 250);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(587, 181);
            this.groupBox1.TabIndex = 5;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "STEP 2";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(99, 155);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(370, 13);
            this.label4.TabIndex = 9;
            this.label4.Text = "=> Finally enter \"App Key\", \"App Secret\" and \"Refresh Token\" in config.json";
            // 
            // textBoxRefreshToken
            // 
            this.textBoxRefreshToken.Location = new System.Drawing.Point(102, 117);
            this.textBoxRefreshToken.Name = "textBoxRefreshToken";
            this.textBoxRefreshToken.ReadOnly = true;
            this.textBoxRefreshToken.Size = new System.Drawing.Size(462, 20);
            this.textBoxRefreshToken.TabIndex = 8;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(15, 120);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(81, 13);
            this.label2.TabIndex = 6;
            this.label2.Text = "Refresh Token:";
            // 
            // buttonRefreshToken
            // 
            this.buttonRefreshToken.Location = new System.Drawing.Point(102, 79);
            this.buttonRefreshToken.Name = "buttonRefreshToken";
            this.buttonRefreshToken.Size = new System.Drawing.Size(462, 23);
            this.buttonRefreshToken.TabIndex = 7;
            this.buttonRefreshToken.Text = "Get Refresh Token";
            this.buttonRefreshToken.UseVisualStyleBackColor = true;
            this.buttonRefreshToken.Click += new System.EventHandler(this.buttonRefreshToken_Click);
            // 
            // textBoxAccessCode
            // 
            this.textBoxAccessCode.Location = new System.Drawing.Point(102, 36);
            this.textBoxAccessCode.Name = "textBoxAccessCode";
            this.textBoxAccessCode.Size = new System.Drawing.Size(462, 20);
            this.textBoxAccessCode.TabIndex = 6;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(23, 39);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(73, 13);
            this.label1.TabIndex = 6;
            this.label1.Text = "Access Code:";
            // 
            // Main
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(675, 481);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.groupBoxInput);
            this.Name = "Main";
            this.Text = "Dropbox Helper";
            this.groupBoxInput.ResumeLayout(false);
            this.groupBoxInput.PerformLayout();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.TextBox textBoxAppKey;
        private System.Windows.Forms.Label labelKey;
        private System.Windows.Forms.Label labelSecret;
        private System.Windows.Forms.TextBox textBoxAppSecret;
        private System.Windows.Forms.GroupBox groupBoxInput;
        private System.Windows.Forms.Button buttonAccessCode;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button buttonRefreshToken;
        private System.Windows.Forms.TextBox textBoxAccessCode;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox textBoxRefreshToken;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
    }
}

