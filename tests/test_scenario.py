from src.command_runner import CommandRunner


# TODO: this test is quite rudimentary and not so easy to read and/or maintain
# Also, we're missing other kinds of tests (e.g. more granular)
def test_scenario():
    runner = CommandRunner()

    inputs = [
        "DEPEND TELNET TCPIP NETCARD",
        "DEPEND TCPIP NETCARD",
        "DEPEND DNS TCPIP NETCARD",
        "DEPEND BROWSER TCPIP HTML",
        "INSTALL NETCARD",
        "INSTALL TELNET",
        "INSTALL foo",
        "REMOVE NETCARD",
        "INSTALL BROWSER",
        "INSTALL DNS",
        "LIST",
        "REMOVE TELNET",
        "REMOVE NETCARD",
        "REMOVE DNS",
        "REMOVE NETCARD",
        "INSTALL NETCARD",
        "REMOVE TCPIP",
        "REMOVE BROWSER",
        "REMOVE TCPIP",
        "LIST",
        "END",
    ]
    outputs = [
        [],
        [],
        [],
        [],
        ["NETCARD successfully installed"],
        ["TELNET successfully installed", "TCPIP successfully installed"],
        ["foo successfully installed"],
        ["NETCARD is still needed"],
        ["BROWSER successfully installed", "HTML successfully installed"],
        ["DNS successfully installed"],
        ["NETCARD", "TELNET", "DNS", "TCPIP", "foo", "BROWSER", "HTML"],
        ["TELNET successfully removed"],
        ["NETCARD is still needed"],
        ["DNS successfully removed"],
        ["NETCARD is still needed"],
        ["NETCARD is already installed"],
        ["TCPIP is still needed"],
        [
            "BROWSER successfully removed",
            "TCPIP is no longer needed",
            "TCPIP successfully removed",
            "HTML is no longer needed",
            "HTML successfully removed",
        ],
        ["TCPIP is not installed"],
        ["NETCARD", "foo"],
    ]

    for input, output in zip(inputs, outputs):
        assert sorted(runner.run_command(input)) == sorted(output)
