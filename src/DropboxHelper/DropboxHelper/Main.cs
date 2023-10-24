using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text.RegularExpressions;
using System.Windows.Forms;

namespace DropboxAppData
{
    public partial class Main : Form
    {
        private string ACCESS_CODE_URI =
            "https://www.dropbox.com/oauth2/authorize?client_id={0}&response_type=code&token_access_type=offline";

        HttpClient Client = new HttpClient();

        public Main()
        {
            InitializeComponent();
        }

        private void buttonAccessCode_Click(object sender, EventArgs e)
        {
            System.Diagnostics.Process.Start(string.Format(ACCESS_CODE_URI, textBoxAppKey.Text.Trim()));        
        }

        private async void buttonRefreshToken_Click(object sender, EventArgs e)
        {
            var requestContent = new FormUrlEncodedContent(new[] {
                    new KeyValuePair<string, string>("code", textBoxAccessCode.Text.Trim()),
                    new KeyValuePair<string, string>("grant_type", "authorization_code"),
                    new KeyValuePair<string, string>("client_id", textBoxAppKey.Text.Trim()),
                    new KeyValuePair<string, string>("client_secret", textBoxAppSecret.Text.Trim()),
            });

            var response = await Client.PostAsync("https://api.dropbox.com/oauth2/token", requestContent);
            var jsonResponse = await response.Content.ReadAsStringAsync();

            if (response.IsSuccessStatusCode)
            {
                Match match = new Regex(@"""refresh_token"":.*""(.*)""", RegexOptions.Multiline).Match(jsonResponse);
                if (match.Success)
                {
                    textBoxRefreshToken.Text = match.Groups[1].Value;
                }
                else
                {
                    textBoxRefreshToken.Text = "Error: Cannot find refresh token in json response.";
                }
            }
            else
            {
                textBoxRefreshToken.Text = jsonResponse;
            }
        }
    }
}
