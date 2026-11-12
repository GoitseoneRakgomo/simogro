from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def home():
        return render_template("index.html")

    @app.get("/privacy")
    def privacy():
        return render_template(
            "policy.html",
            title="Privacy notice",
            heading_first="Privacy",
            heading_second="notice.",
            summary="How information is handled when you visit the Simogro website or contact the company.",
            sections=[
                {
                    "heading": "Information and use",
                    "paragraphs": [
                        "This website does not provide visitor accounts or an onsite enquiry form. It currently uses no analytics or advertising cookies. A browser storage preference remembers whether you accepted or rejected optional cookies; optional cookies will only be used if you accept.",
                        "If you contact Simogro by email, the information you submit may be used to consider your correspondence and maintain appropriate records. Information may be handled or disclosed where required by applicable law.",
                    ],
                },
                {
                    "heading": "Hosting and enquiries",
                    "paragraphs": [
                        "Any production hosting provider may process normal server logs. For enquiries concerning correspondence sent to the company, use the contact details on the home page.",
                        "This is a preliminary notice and requires legal approval before publication.",
                    ],
                },
            ],
        )

    @app.get("/terms")
    def terms():
        return render_template(
            "policy.html",
            title="Terms of use",
            heading_first="Terms",
            heading_second="of use.",
            summary="Important information about the material published on this website.",
            sections=[
                {
                    "heading": "Website information",
                    "paragraphs": [
                        "Information published on this website is general corporate background only, supplied without representations concerning the suitability or availability of any transaction or service. Nothing on this site constitutes an offer, solicitation or investment recommendation.",
                    ],
                },
                {
                    "heading": "Use of this website",
                    "paragraphs": [
                        "The content is subject to change. No contractual, advisory or other relationship is formed merely by visiting the site or sending an enquiry. These terms remain subject to legal review.",
                    ],
                },
            ],
        )

    @app.get("/cookie-settings")
    def cookie_settings():
        return render_template(
            "policy.html",
            title="Cookie settings",
            heading_first="Cookie",
            heading_second="settings.",
            summary="Review and update your optional cookie preference for this browser.",
            cookie_settings=True,
            sections=[
                {
                    "heading": "Current use",
                    "paragraphs": [
                        "This site currently uses no analytics or advertising cookies. Your choice to accept or reject optional cookies is saved in this browser’s local storage. No optional cookies are currently configured.",
                    ],
                },
                {
                    "heading": "Your preference",
                    "paragraphs": [
                        "Choose whether to accept or reject optional cookies. If optional cookies are introduced in future, this page should be updated to describe them.",
                    ],
                },
            ],
        )

    return app


app = create_app()


if __name__ == "__main__":
    app.run()
