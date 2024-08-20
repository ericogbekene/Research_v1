import { Button } from "./button";
import Link from "next/link";
import Image from "next/image";

const Hero = () => {
    return (
        <>
            <section className="container mx-auto bg-slate-300 flex flex-col px-8 py-36 sm:flex-row-reverse sm:px-12">
                
                    <img
                        alt="Woman doing meditation"
                        className="mb-8 w-full sm:mb-0 sm:ml-4 sm:w-1/2 dark:contrast-200"
                        src="/images/undraw_creation_process.svg"
                    />

                <div className="mr-4 w-full text-center sm:w-1/2 sm:text-left">
                    <h1 className="mb-4 text-3xl font-bold leading-tight dark:text-dark-50 md:text-4xl">
                        Train your mind,
                        <br /> be peaceful
                    </h1>
                    <p className="mb-8 leading-relaxed text-slate-700 dark:text-slate-400">
                        Browse Our Collection of Expertly written Academic Papers
                    </p>
                    <Button asChild>
                        <Link href="/hire-writer"> Register now </Link>

                    </Button>
                </div>
            </section>
        </>
    );
}

export default Hero;