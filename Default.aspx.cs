using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using Npgsql;

namespace WebApplication1
{
    public partial class Default : System.Web.UI.Page
    {
        

        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void Button1_Click(object sender, EventArgs e)
        {
            string connstring = String.Format("Server={0};Port={1};" +
                    "User Id={2};Password={3};Database={4};",
                    "localhost", "5432", "postgres",
                    "1234asdf", "movies");
            
            // Making connection with Npgsql provider
            NpgsqlConnection conn = new NpgsqlConnection(connstring);
            conn.Open();
            //var str;
            string t = title.Text;
            string q = "SELECT movieid from movies WHERE title=" + t;
            var cmd = new NpgsqlCommand(q, conn);
            var reader = cmd.ExecuteReader();
            while (reader.Read())
            {
                try
                {
                    tag.Text = reader.GetString(0);
                }
                catch
                {

                }
                
            }
                


                conn.Close();
        }

        protected void Chart1_Load(object sender, EventArgs e)
        {

        }

        protected void submit_Click(object sender, EventArgs e)
        {
            string connstring = String.Format("Server={0};Port={1};" +
                    "User Id={2};Password={3};Database={4};",
                    "localhost", "5432", "postgres",
                    "1234asdf", "movies");

            // Making connection with Npgsql provider
            NpgsqlConnection conn = new NpgsqlConnection(connstring);
            conn.Open();
            //var str;
            long i;
            string s;
            string t = title.Text;
            string q = "SELECT g.name AS name, COUNT(g.genreid) AS moviecount FROM movies m, hasagenre h, genres g WHERE m.movieid = h.movieid AND h.genreid = g.genreid GROUP BY g.genreid";
            var cmd = new NpgsqlCommand(q, conn);
            var reader = cmd.ExecuteReader();
            while (reader.Read())
            {
                try
                {

                    t = reader.GetString(0);
                    i = reader.GetInt64(1);
                    //Console.WriteLine(reader.GetString(0));
                }
                catch
                {

                }

            }

            //charts.

            conn.Close();
        }
    }
}